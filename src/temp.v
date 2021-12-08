module or2_16 (input wire a[15:0], output wire y);	// Declaring temporary wires
	temp[1:0];
	// Module definition
	or2_8 or2_8_0(a[7:0], temp[0]);
	or2_8 or2_8_0(a[15:8], temp[0]);
	// Combiner Logic
	or2_2 or2_2_2(temp[1:0], y);
endmodule

module or2_4 (input wire a[3:0], output wire y);	// Declaring temporary wires
	temp[1:0];
	// Module definition
	or2_2 or2_2_0(a[1:0], temp[0]);
	or2_2 or2_2_0(a[3:2], temp[0]);
	// Combiner Logic
	or2_2 or2_2_2(temp[1:0], y);
endmodule

module or2_8 (input wire a[7:0], output wire y);	// Declaring temporary wires
	temp[1:0];
	// Module definition
	or2_4 or2_4_0(a[3:0], temp[0]);
	or2_4 or2_4_0(a[7:4], temp[0]);
	// Combiner Logic
	or2_2 or2_2_2(temp[1:0], y);
endmodule

module myor15 (input wire a[14:0], output wire y);	// Declaring temporary wires
	temp[3:0];
	// Module definition
	or2_8 or2_8_0(a[7:0], temp[0]);
	or2_4 or2_4_1(a[11:8], temp[1]);
	or2_2 or2_2_2(a[13:12], temp[2]);
	assign temp[3] = a[14];
	// Combiner Logic
	or2_4 or2_4_4(temp[3:0], y);
endmodule

module myor32 (input wire a[31:0], output wire y);	// Declaring temporary wires
	temp[1:0];
	// Module definition
	or2_16 or2_16_0(a[15:0], temp[0]);
	or2_16 or2_16_0(a[31:16], temp[0]);
	// Combiner Logic
	or2_2 or2_2_2(temp[1:0], y);
endmodule

module or2_2 (input wire a[1:0], output wire y);
    assign y = a[1] | a[0];
endmodule