



"""
Working through an example like "hello!"

Ask for the message first.

Starting with h, I have 1
then with e, I have 1 of those.
then with l, one of those!
another l.  two of those.
an ! ... one other character.

I need to make a bucket for each letter,
and set each count to 0.

I will probably need a bucket for each of the letters
and then another bucket for other stuff.

Then I will go through the letters,
figure out which bucket is associated with it,
then add one to the count in that bucket.

Then display the data.

"""

def initializeBuckets():
    """ make a list of zeros for all buckets """
    return [0] * 27

def findBucketNum(someChar):
    """ find the bucket num for the char """
    someChar = someChar.lower() # force char to lowercase
    # how far is someChar away from "a" ?
    distanceFromA = ord(someChar) - ord('a')
    if someChar not in "abcdefghijklmnopqrstuvwxyz":
        result = 26
    else:
        result = distanceFromA
    return result

LETTERS = "abcdefghijklmnopqrstuvwxyz"

def getBucketsAsString(buckets):
    result = ""
    # use ! as label for other characters in histo
    for char in LETTERS + "!":
        bNum = findBucketNum(char)
        result = result + char + ": " + "  "\
                 "{:3d}  ".format(buckets(bNum]) +  \
                 "x" * buckets(bNum)

    return result


# what would   return str(buckets) do ?




def main():
    """ This is our main routine! """
    text = input("What's the text? ")

    buckets = initializeBuckets()
    for eachChar in text:
        bucketNum = findBucketNum(eachChar)
        buckets[bucketNum] = buckets[bucketNum] + 1
    bucketStr = getBucketsAsString(buckets)
    print("The histogram for your message is:", bucketStr)


def unitTest_findBucketNum():
    """ this function runs all the tests for findBucketNum! """
    if (findBucketNum('A') != 0):
        print("Error for A !")
    if (findBucketNum('z') != 25):
        print("Error for z!")
    if (findBucketNum('!') != 26):
        print("Error for !  !!!")

def unitTest_getBucketsAsString():
    print(getBucketsAsString( [0] * 26 + [0] ))
    print(getBucketsAsString( [3] * 26 + [3] ))

if __name__ == "__main__":
    unitTest_findBucketNum()
    unitTest_getBucketsAsString()
    #main()
