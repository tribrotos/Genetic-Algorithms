import numpy

target = str(input("Target : "))
panjang_target = len(target)

def create_gen (panjang_gen) :
    hasil = ""
    random_number = numpy.random.randint(32,126,(1,panjang_gen))
    for i in range(panjang_gen):
        hasil = hasil + chr(random_number[0][i])
    return hasil

def calculate_fitness (gen,target,panjang_gen):
    count = 0
    for i in range (panjang_gen):
        if (target[i] == gen[i]):
            count = count + 1
    hasil = count/len(target)*100
    return hasil

gen_baru = create_gen(panjang_target)
fitness = calculate_fitness(gen_baru,target,panjang_target)

print("New Gen : "+str(gen_baru))
print("Fitness Value: "+str(fitness)+" %")
