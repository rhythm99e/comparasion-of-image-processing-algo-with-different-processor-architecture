class Processor:
    def __init__(self,name,specs):
        self.name=name
        self.clock_speed=specs["clock_speed"]
        self.ipc=specs["ipc"]
        self.simd_width=specs["simd_width"]
        self.memory_bandwidth=specs["memory_bandwidth"]
        self.power=specs["power"]
    def __return__(self):
        return {
            "name": self.name,
            "clock_speed": self.clock_speed,
            "ipc": self.ipc,
            "simd_width": self.simd_width,
            "memory_bandwidth": self.memory_bandwidth,
            "power": self.power
    }
processor_o={#making a dictioinay for easy access
    "mips":Processor("MIPS",{# data might not be accurate cloud sanga manga ko ho
        "clock_speed": 1.5,  #ghz 
        "ipc":2,#this tells how many instruction can be executed in each clock cycle
        "simd_width": 4,#this gives the concept of parallelism  
        "memory_bandwidth": 8,#gb/s  
        "power": 2  
          }),
    "RISC-V":Processor("RISC-V",{
        "clock_speed": 2,  
        "ipc": 3,
        "simd_width": 8,  
        "memory_bandwidth": 16,  
        "power": 4
    }),
    "ARM":Processor("ARM",{
        "clock_speed": 3,  
        "ipc": 5,
        "simd_width": 4,  
        "memory_bandwidth": 51,  
        "power": 5 
    }),
    "asic":Processor("ASIC",{
        "clock_speed": 1,  
        "ipc": 32,
        "simd_width": 64,  
        "memory_bandwidth": 200,  
        "power": 3 
    }),
    "intel":Processor("Intel",{
        "clock_speed": 4.7, 
        "ipc": 6,
        "simd_width": 16,  
        "memory_bandwidth": 51,  
        "power": 28
    }),
}