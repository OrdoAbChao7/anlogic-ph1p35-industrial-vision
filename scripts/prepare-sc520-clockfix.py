"""Create an isolated SC520 Lab1 work copy with the reviewed clock changes.

Requires the local vendor work copy in .tools/td/work/lab_ex1_mipi_hdmi_sc520.
The vendor source and generated TD files stay outside Git.
"""

from __future__ import annotations

import argparse
import re
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / ".tools" / "td" / "work"
SOURCE = WORK / "lab_ex1_mipi_hdmi_sc520"
DEFAULT_TARGET = WORK / "lab_ex1_mipi_hdmi_sc520_clockfix"


def replace_one(text: str, before: str, after: str) -> str:
    count = text.count(before)
    if count != 1:
        raise ValueError(f"Expected one match, found {count}: {before[:70]!r}")
    return text.replace(before, after, 1)


def edit_vendor_file(path: Path, changes: list[tuple[str, str]]) -> None:
    raw = path.read_bytes()
    newline = "\r\n" if b"\r\n" in raw else "\n"
    text = raw.decode("latin1").replace("\r\n", "\n")
    for before, after in changes:
        text = replace_one(text, before, after)
    path.write_bytes(text.replace("\n", newline).encode("latin1"))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--target", type=Path, default=DEFAULT_TARGET)
    args = parser.parse_args()
    target = args.target.resolve()
    if not target.is_relative_to(WORK.resolve()) or target == WORK.resolve():
        raise ValueError("Target must be inside .tools/td/work")
    if target.exists():
        raise FileExistsError(f"Preserving existing work copy: {target}")

    for part in ("user_source", "td_project/al_ip"):
        source_part = SOURCE / part
        if not source_part.exists():
            raise FileNotFoundError(source_part)
        shutil.copytree(source_part, target / part)

    project_dir = target / "td_project"
    for name in ("camera_to_dsi_display.al", "camera_to_dsi_display.sdc"):
        shutil.copy2(SOURCE / "td_project" / name, project_dir / name)
    al = project_dir / "camera_to_dsi_display.al"
    xml = al.read_text(encoding="utf-8")
    xml, count = re.subn(
        r'(?<=<Project Version="3" Minor="2" )Path="[^"]+"',
        f'Path="{project_dir.as_posix()}"',
        xml,
        count=1,
    )
    if count != 1:
        raise ValueError("TD project root path not found")
    al.write_text(xml, encoding="utf-8")

    top = target / "user_source/hdl_source/design_top_wrapper.v"
    edit_vendor_file(top, [
        (
            "assign O_cam_24m \t= S_24m_clk;",
            "// Drive the sensor MCLK through an output DDR register. Keep the PLL\n"
            "    // clock net dedicated to internal clock pins and the ODDR clock input.\n"
            "    PH1P_LOGIC_HD_ODDR u_cam_mclk_out (\n"
            "        .clk(S_24m_clk),\n"
            "        .rst(~S_pll_lock),\n"
            "        .d0(1'b1),\n"
            "        .d1(1'b0),\n"
            "        .q(O_cam_24m)\n"
            "    );",
        ),
    ])

    i2c = target / "user_source/hdl_source/uics500_cfg/uii2c.v"
    edit_vendor_file(i2c, [
        (
            "wire scl_offset;",
            "// Keep all I2C state in I_clk; pulse once at each former divided-clock edge.\n"
            "wire scl_pos_en = (clkdiv == SCL_DIV) && !scl_clk;\n"
            "wire scl_neg_en = (clkdiv == SCL_DIV) &&  scl_clk;\n"
            "wire scl_offset;",
        ),
        (
            "always @(posedge scl_clk) \n    if(IIC_S == W_ACK",
            "always @(posedge I_clk)\n    if (scl_pos_en) begin\n    if(IIC_S == W_ACK",
        ),
        (
            "        sda_r <= sda_r;\n\n//sda data bus",
            "        sda_r <= sda_r;\n    end\n\n//sda data bus",
        ),
        (
            "always @(negedge scl_clk)begin",
            "always @(posedge I_clk) if (scl_neg_en) begin",
        ),
        (
            "always @(posedge scl_clk or negedge I_rstn )begin\n\tif(I_rstn == 1'b0)",
            "always @(posedge I_clk or negedge I_rstn )begin\n\tif(I_rstn == 1'b0)",
        ),
        (
            "always @(posedge scl_clk or negedge I_rstn )begin\n\t\tif(I_rstn == 1'b0)begin",
            "always @(posedge I_clk or negedge I_rstn )begin\n\t\tif(I_rstn == 1'b0)begin",
        ),
        (
            "always @(negedge scl_clk or negedge I_rstn )begin",
            "always @(posedge I_clk or negedge I_rstn )begin",
        ),
        (
            "O_iic_busy <= 1'b0; \n\telse begin",
            "O_iic_busy <= 1'b0; \n\telse if (scl_pos_en) begin",
        ),
        (
            "O_iic_bus_error <= 1'b0;  \t\n\telse begin",
            "O_iic_bus_error <= 1'b0;  \t\n\telse if (scl_neg_en) begin",
        ),
        (
            "IIC_S    <= IDLE;\n        end\n        else begin",
            "IIC_S    <= IDLE;\n        end\n        else if (scl_pos_en) begin",
        ),
    ])

    print(f"Created SC520 clockfix project: {al}")


if __name__ == "__main__":
    main()
