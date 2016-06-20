-- File: gray_inc_reg.vhd
-- Generated by MyHDL 1.0dev
-- Date: Mon May 23 18:06:58 2016


library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.numeric_std.all;
use std.textio.all;

use work.pck_myhdl_10.all;

entity gray_inc_reg is
    port (
        graycnt: out unsigned(7 downto 0);
        enable: in std_logic;
        clock: in std_logic;
        reset: in std_logic
    );
end entity gray_inc_reg;


architecture MyHDL of gray_inc_reg is


signal graycnt_comb: unsigned(7 downto 0);
signal gray_inc_0_bincnt: unsigned(7 downto 0);

begin




GRAY_INC_REG_GRAY_INC_0_INC_1_SEQ: process (clock, reset) is
begin
    if (reset = '0') then
        gray_inc_0_bincnt <= to_unsigned(0, 8);
    elsif rising_edge(clock) then
        if bool(enable) then
            gray_inc_0_bincnt <= (gray_inc_0_bincnt + 1);
        end if;
    end if;
end process GRAY_INC_REG_GRAY_INC_0_INC_1_SEQ;


graycnt_comb <= (shift_right(gray_inc_0_bincnt, 1) xor gray_inc_0_bincnt);

GRAY_INC_REG_REG_0: process (clock, reset) is
begin
    if (reset = '0') then
        graycnt <= to_unsigned(0, 8);
    elsif rising_edge(clock) then
        graycnt <= graycnt_comb;
    end if;
end process GRAY_INC_REG_REG_0;

end architecture MyHDL;
