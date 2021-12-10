module ripplecarryadder16(input wire a[7:0], wire b[7:0], wire cin, output wire y[7:0], wire z);
	// Declaring temporary wires
	temp[7:0];
	// Module definition
	fa fa_0(a[0], b[0], cin, y[0], temp[0]);
	fa fa_1(a[1], b[1], temp[0], y[1], temp[1]);
	fa fa_2(a[2], b[2], temp[1], y[2], temp[2]);
	fa fa_3(a[3], b[3], temp[2], y[3], temp[3]);
	fa fa_4(a[4], b[4], temp[3], y[4], temp[4]);
	fa fa_5(a[5], b[5], temp[4], y[5], temp[5]);
	fa fa_6(a[6], b[6], temp[5], y[6], temp[6]);
	fa fa_7(a[7], b[7], temp[6], y[7], z);

endmodule


