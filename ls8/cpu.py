"""CPU functionality."""

import sys

class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        self.ram = bytearray([0] * 256)
        self.reg = bytearray([0] * 7 + [0xF4])
        # Internal registers:        
        self.pc = 0  # PC: Program Counter, address of the currently executing instruction
        self.ir = 0  # Instruction Register, contains a copy of the currently executing instruction
        self.mar = 0  # Memory Address Register, holds the memory address we're reading or writing
        self.mdr = 0  # Memory Data Register, holds the value to write or the value just read
        self.fl = [0b00000000]  # Flag

        self.ir = {0b00000001: self.HLT,
                   0b10000010: self.LDI,
                   0b01000111: self.PRN}

    def ram_read(self, mar):
        return self.ram[mar]  # Accepts the address to read and return the value stored there

    def ram_write(self, mdr, mar):
        self.ram[mar] = mdr  # Accepts a value to write, and the address to write it to

    def load(self):
        """Load a program into memory."""

        address = 0

        # For now, we've just hardcoded a program:

        program = [
            # From print8.ls8
            0b10000010, # LDI R0,8
            0b00000000,
            0b00001000,
            0b01000111, # PRN R0
            0b00000000,
            0b00000001] # HLT

        for instruction in program:
            self.ram[address] = instruction
            address += 1


    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        #elif op == "SUB": etc
        else:
            raise Exception("Unsupported ALU operation")


    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            #self.fl,
            #self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()


    def run(self):
        """Run the CPU."""
        while True:
            index = self.ram[self.pc]

            # Get dictionary entry then execute returned instruction
            next_step = self.ir[index]
            next_step()


    def LDI(self):
        # Set a specified register to a specified value
        address = self.ram_read(self.pc + 1)
        value = self.ram_read(self.pc + 2)
        # Write the value to the registry at specified address
        self.reg[address] = value
        self.pc += 3


    def PRN(self):
        # Print numeric value stored in the given register
        address = self.ram_read(self.pc + 1)
        print(self.reg[address])
        self.pc += 2


    def HLT(self):
        sys.exit(0)
