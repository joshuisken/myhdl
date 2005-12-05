from myhdl import Signal, delay, always, now, Simulation

def sayHello():
    
    @always(delay(10))
    def behavior():
        print "%s Hello World!" % now()

    return behavior


def main():
    sim = Simulation(sayHello())
    sim.run(30)
    

if __name__ == '__main__':
    main()


