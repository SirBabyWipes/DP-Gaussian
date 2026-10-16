import numpy as np


# parses data from csv file into a list
def readFile(fileToRead):
    data = []
    with open(fileToRead, "r", encoding="utf-8")as file:
        next(file)
        for line in file:
            age, gender = line.strip().split(',')
            data.append([int(age), int(gender)])
    return data

# takes parsed data and puts it into a dict of counts for each datapoint
def trueBins(data):
    trueBins = {(age, gender): 0
              for age in range(17, 91)
              for gender in (1, 2)}
    
    for age, gender in data:
        trueBins[(age, gender)] += 1


    return trueBins


# takes truebins and adds noise to them
def gaussian(trueBins, epsilon, delta):
    sigma = (1 / epsilon) * np.sqrt(2* np.log(1.25 / delta))
    noisyBins = {}

    for key, count in trueBins.items():
        value = count + np.random.normal(0, sigma)
        noisyBins[key] = max(round(value), 0)


    return noisyBins


# calculates mean error between true and noisy bin counts
def mae(trueBins, noisyBins):
    MAE = 0.0
    for key in trueBins.keys():
        bin = trueBins[key]
        noiseBin = noisyBins[key]
        difference = bin -noiseBin
        MAE += abs(difference)

    MAE = MAE / len(trueBins)
    return MAE


def main():
    delta = 0.00001
    epsilon = input("Enter your epsilon: ")
    epsilon = float(epsilon)
    data = readFile('adult_age_gender_dataset.csv')
    trueCount = trueBins(data)
    #print (trueCount)
    noisyCount = gaussian(trueCount, epsilon, delta)
    #print("------------------------------------------------------------------------------")
    #print(noisyCount)
    meanError = mae(trueCount, noisyCount)
    print(meanError)



main()

