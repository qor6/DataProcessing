##########################################################################
## BigData Analytics: BA_CSE418_lastname_id.py
## 
## 과제1과 2에 대한 템플릿 코드
## #[TODO]# 라고 표기된 지역에만 코드를 작성하시기 바랍니다.
##
## 학생 이름:백수민
## 학번:2143993


import sys
from pprint import pprint
from random import random
from collections import deque
from sys import getsizeof
import resource
import hashlib

##########################################################################
##########################################################################
# 풀이: 아래 4가지 메소드를 주어진 메모리 변수에 각각 맞추어 구현하시기 바랍니다.
#
# 각 메소드는 amount를 100개 크기의 메모리 배열을 가진다.
# 메모리 배열의 변수명은 memory1a, memory1b, memory1c, memory1d 이다.
# 따라서, 주어진 메모리 배열 이외에 데이터 저장을 위한 새로운 변수선언은 금지한다
# 현재 메모리의 크기는 8,000을 넘지 않도록 설계되어 있음.

MEMORY_SIZE = 100 #do not edit

memory1a =  deque([None] * MEMORY_SIZE, maxlen=MEMORY_SIZE) #do not edit

def task1AReservoirSampling(element, returnResult = True):
    # [TODO]#
    # process the element you may only use memory1a, storing at most 100
    global memory1a

    if returnResult:  # when the stream is requesting the current result (e.g., sum )
        # result = 0
        # [TODO]#
        if len(memory1a) < MEMORY_SIZE:
            memory1a.append(element)
        else:
            rand_index = int(random() * MEMORY_SIZE)
            if rand_index < MEMORY_SIZE:
                memory1a[rand_index] = element
        result = sum(filter(None, memory1a))
        # any additional processing to return the result at this point
        return result
    else:  # no need to return a result
        pass

memory1b = deque([None] * MEMORY_SIZE, maxlen=MEMORY_SIZE)  # do not edit

def task2BDistinctAmount(element, returnResult = True):
    # [TODO]#
    # process the element you may only use memory1a, storing at most 100
    global memory1b
    
    if returnResult: #when the stream is requesting the current result
        # result = 0
        #[TODO]#
        hashed_values = set()
        for i in range(MEMORY_SIZE):
            hashed_value = hashlib.sha256(str(element).encode('utf-8') + str(i).encode('utf-8')).hexdigest()
            hashed_values.add(hashed_value)

        max_trailing_zeros = 0
        for hashed_value in hashed_values:
            binary_representation = bin(int(hashed_value, 16))[2:][::-1]
            trailing_zeros = len(binary_representation) - len(binary_representation.lstrip('0'))
            max_trailing_zeros = max(max_trailing_zeros, trailing_zeros)

        distinct_estimate = 2 ** max_trailing_zeros
        result = distinct_estimate
        #any additional processing to return the result at this point
        return result
    else: #no need to return a result
        pass


memory1c =  deque([None] * MEMORY_SIZE, maxlen=MEMORY_SIZE) #do not edit

def task3CMedian(element, returnResult = True):
    #[TODO]#
    # process the element you may only use memory1a, storing at most 100
    global memory1c

    if returnResult: #when the stream is requesting the current result
        # result = 0
        #[TODO]#
        if len(memory1c) < MEMORY_SIZE:
            memory1c.append(element)
        else:
            rand_index = int(random() * MEMORY_SIZE)
            if rand_index < MEMORY_SIZE:
                memory1c[rand_index] = element
        filtered_memory = [value for value in memory1c if value is not None]
        sorted_memory = sorted(filtered_memory)
        cdf = [i / len(sorted_memory) for i in range(1, len(sorted_memory) + 1)]

        median_index = min(range(len(cdf)), key=lambda i: abs(cdf[i] - 0.5))
        result = sorted_memory[median_index]
        #any additional processing to return the result at this point
        return result
    else: #no need to return a result
        pass
    

memory1d =  deque([None] * MEMORY_SIZE, maxlen=MEMORY_SIZE) #do not edit

def task4DMostFreqAmount(element, returnResult = True):
    #[TODO]#
    # process the element you may only use memory1a, storing at most 100
    
    if returnResult: #when the stream is requesting the current result
        # result = 0
        #[TODO]#
        if len(memory1d) < MEMORY_SIZE:
            memory1d.append(element)
        else:
            rand_index = int(random() * MEMORY_SIZE)
            if rand_index < MEMORY_SIZE:
                memory1d[rand_index] = element

        counts = {value: memory1d.count(value) for value in memory1d}
        most_freq_value = max(counts, key=counts.get)
        result = most_freq_value if most_freq_value is not None else 0
        #any additional processing to return the result at this point
        return result
    else: #no need to return a result
        pass


##########################################################################
##########################################################################
# MAIN 함수: 해당 코드는 파일로부터 스트림을 불러오고 각 작업에 대한 함수를 호출한다.
# 반환되는 결과의 출력은 자주 수행될 수 있다.
# 가능하면 아래의 코드를 수정하지 마시오
# 물론, 보너스 문제에 대해서는 수정이 가능하다.

def getMemorySize(l): #returns sum of all element sizes
    return sum([getsizeof(e) for e in l])+getsizeof(l)

if __name__ == "__main__": #[Uncomment peices to test]
    
    print("\n\nTESTING YOUR CODE\n")
    
    ###################
    ## The main stream loop: 
    print("\n\n*************************\n Beginning stream input \n*************************\n")
    filename = sys.argv[1] # the data file to read into a stream
    printLines = frozenset([10**i for i in range(1, 20)]) #stores lines to print
    peakMem = 0 #tracks peak memory usage
    
    with open(filename, 'r') as infile:
        i = 0 # keeps track of lines read
        for line in infile:
        
            # remove \n and convert to int
            element = int(line.strip())
            i += 1
            
            # call tasks
            if i in printLines: # print status at this point:
                result1a = task1AReservoirSampling(element, returnResult=True)
                result1b = task2BDistinctAmount(element, returnResult=True)
                result1c = task3CMedian(element, returnResult=True)
                result1d = task4DMostFreqAmount(element, returnResult=True)
                
                print(" Result at stream element # %d:" % i)
                print("   1A:  Sum value(by Reservoir Sampling): %d" % int(result1a))
                print("   2B:                   Distinct values: %d" % int(result1b))
                print("   3C:                            Median: %.2f" % float(result1c))
                print("   4D:               Most frequent value: %d" % int(result1d))
                print(" [current memory sizes: A: %d, B: %d, C: %d, D: %d]\n" % \
                    (getMemorySize(memory1a), getMemorySize(memory1b), getMemorySize(memory1c), getMemorySize(memory1d)))
                
            else: # just pass for stream processing
                result1a = task1AReservoirSampling(element, False)
                result1b = task2BDistinctAmount(element, False)
                result1c = task3CMedian(element, False)
                result1d = task4DMostFreqAmount(element, False)

            memUsage = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
            if memUsage > peakMem: peakMem = memUsage
        
    print("\n*******************************\n       Stream Terminated \n*******************************")
    print("(peak memory usage was: ", peakMem, ")")