// File: Inc.v
// Generated by MyHDL 0.7
// Date: Sun Dec 19 16:52:33 2010


`timescale 1ns/10ps

module Inc (
    count,
    enable,
    clock,
    reset
);
// Incrementer with enable.
// 
// count -- output
// enable -- control input, increment when 1
// clock -- clock input
// reset -- asynchronous reset input
// n -- counter max value

output [7:0] count;
reg [7:0] count;
input enable;
input clock;
input reset;






always @(posedge clock, negedge reset) begin: INC_INCLOGIC
    if ((reset == 0)) begin
        count <= 0;
    end
    else begin
        if (enable) begin
            count <= ((count + 1) % 256);
        end
    end
end

endmodule
