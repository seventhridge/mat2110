

"""
We have a list of bucket sizes, and a list of bucket contents.

Operation  i->j  fill bucket j with i until i is empty or j is full either one.
Operation  fi    fill bucket i from fawcet
operation  di    dump bucket i

Solution:  bucket i has N gallons in it.


"""

MAX_MOVES = 200

def solveBuckets(targetBucket, targetGallons, buckets, sizes, solutionSoFar = "", configsSeenSoFar = [], depth=0):
    if str(buckets) in configsSeenSoFar or depth > MAX_MOVES:
        return ""
    if buckets[targetBucket] == targetGallons:
        return "Solved in " + str(depth) + "! Here's how: \n" + solutionSoFar
    else:
        #print("  " * depth, "Buckets now: ", str(buckets))
        configsSeenSoFar.append(str(buckets))
        # See if moving from i to j works.
        bestResult = ""
        for bucketI in range(len(buckets)):
            for bucketJ in range(len(buckets)):
                if bucketI != bucketJ and buckets[bucketI] > 0 and buckets[bucketJ] < sizes[bucketJ]:
                    #print("  " * depth,"Try moving bucket", bucketI, "to", bucketJ)
                    newBuckets = buckets[:]
                    # put into J as much as we can from I.
                    newBuckets[bucketJ] = min( sizes[bucketJ], buckets[bucketI] + buckets[bucketJ])
                    # take out of I the amount we put into J.
                    newBuckets[bucketI] = buckets[bucketI] -  ( newBuckets[bucketJ] - buckets[bucketJ])
                    newSolutionSoFar = solutionSoFar + " " + str(bucketI)+"->"+str(bucketJ)
                    result = solveBuckets(targetBucket, targetGallons, newBuckets, sizes,
                                          newSolutionSoFar, configsSeenSoFar, depth+1)
                    #if we found a result and the result is smaller than the best result so far
                    if result and (not bestResult or len(result) < len(bestResult)):
                        bestResult = result

        # okay none of that worked.
        # See if draining a bucket not empty works.
        for bucket in range(len(buckets)):
            if buckets[bucket] > 0:
                # print("  " * depth,"Try draining bucket", bucket)
                newBuckets = buckets[:]
                newBuckets[bucket] = 0
                newSolutionSoFar = solutionSoFar + " d" + str(bucket)
                result = solveBuckets(targetBucket, targetGallons, newBuckets, sizes,
                                      newSolutionSoFar, configsSeenSoFar, depth + 1)
                if result and (not bestResult or len(result) < len(bestResult)):
                    bestResult = result

                    # okay none of THAT worked.

        # see if filling a bucket not already filled works
        for bucket in range(len(buckets)):
            if buckets[bucket] < sizes[bucket]:
                #print("  " * depth,"Try fill bucket", bucket)
                newBuckets = buckets[:]
                newBuckets[bucket] = sizes[bucket]
                newSolutionSoFar = solutionSoFar + " f" + str(bucket)
                result = solveBuckets(targetBucket, targetGallons, newBuckets, sizes,
                                      newSolutionSoFar, configsSeenSoFar, depth+1)
                if result and (not bestResult or len(result) < len(bestResult)):
                    bestResult = result

        return bestResult

#print (solveBuckets(0, 3, [3], [3]))
#print (solveBuckets(0, 2, [0,0], [4,3]))
print (solveBuckets(0, 2, [0,0,0], [4,31,20]))
