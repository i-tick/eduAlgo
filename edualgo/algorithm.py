import time

def print_msg_box(msg, indent=1, width=None, title=None):
    """Print message-box with optional title."""
    lines = msg.split('\n')
    space = " " * indent
    if not width:
        width = max(map(len, lines))
    box = f'╔{"═" * (width + indent * 2)}╗\n'  # upper_border
    if title:
        box += f'║{space}{title:<{width}}{space}║\n'  # title
        box += f'║{space}{"-" * len(title):<{width}}{space}║\n'  # underscore
    box += ''.join([f'║{space}{line:<{width}}{space}║\n' for line in lines])
    box += f'╚{"═" * (width + indent * 2)}╝'  # lower_border
    print(box)

class sort:

    # bubble sort algorithm
    def bubble_sort(self,arr,hint=False):
        start = time.time()
        for i in range(len(arr)-1):
            for j in range(len(arr)-i-1):
                if arr[j] > arr[j+1] :
                    arr[j],arr[j+1] = arr[j+1],arr[j]
                print(arr)
        end = time.time()
        print("Bubble Sort Runtime = {}".format(end-start))
        if(hint == True):
            self.bubble_sort_hint()
        return arr

    def bubble_sort_hint(self):
        message ="""
        Bubble Sort
        ------------------------------------

        Purpose : sorting in increasing order
        Method : Bubble Making, Swapping

        Time Complexity: Worst Case - O(n^2)

        Hint :
        Try to kick out the greater value to the rightmost position by using loops
        and value swapping.

        Pseudocode:
        --> for i in [0,length of array]
                for j in [0,length of array - 1]
                    if(array[j] > array[i])
                        swap array[j] & array[i]

        Visualization:

        Given Array :

        +-----+-----+-----+
        |  5  |  4  |  3  |
        +-----+-----+-----+

        First Iteration :

        +-----+-----+-----+
        |  4  |  5  |  3  |
        +-----+-----+-----+

        Second Iteration :

        +-----+-----+-----+
        |  4  |  3  |  5  |
        +-----+-----+-----+

        Third Iteration :

        +-----+-----+-----+
        |  3  |  4  |  5  |
        +-----+-----+-----+

        Learn More Here - https://en.wikipedia.org/wiki/Bubble_sort
        """
        print_msg_box(message)

    # selection Sort Algorithm
    def selection_sort(self,arr,hint=False):
        start = time.time()
        for i in range(len(arr)-1):
            minimum = i
            for j in range(i+1,len(arr)):
                if arr[j] < arr[minimum]:
                    minimum = j
            arr[minimum],arr[i] = arr[i],arr[minimum]
            print(arr)
        end = time.time()
        print("Selection Sort Runtime = {}".format(end-start))
        if(hint==True):
            self.selection_sort_hint()
        return arr

    def selection_sort_hint(self):
        message ="""
        selection Sort
        ------------------------------------

        Purpose : sorting in increasing order
        Method : Pick Up minimum, swap with minimum

        Time Complexity: Worst Case - O(n^2)

        Hint :
        In every iteration the minimum element from the unsorted subarray is picked and
        moved to the sorted subarray.

        Pseudocode:
        --> for i in [0,length of array]
                minimum = i
                for j in [i+1,length of array]
                    if arr[j] < arr[minimum]
                        minimum = j
                swap arr[i] & arr[minimum]

        Visualization:

        Given Array :

        +-----+-----+-----+
        |  5  |  4  |  3  |
        +-----+-----+-----+

        We have two buckets,

        |              |        |              |
        |   Unsorted   |        |    sorted    |
        |              |        |              |
        |    5,4,3     |        |     empty    |
         --------------          --------------

        Select the minimum from the unsorted bucket and put that in sorted bucket

        |              |        |              |
        |   Unsorted   |        |    sorted    |
        |              |        |              |
        |     5,4      |        |      3       |
         --------------          --------------

        Again select the minimum from the unsorted bucket and put that in
        sorted bucket

        |              |        |              |
        |   Unsorted   |        |    sorted    |
        |              |        |              |
        |      5       |        |     3,4      |
         --------------          --------------

        Repeat the same till the unsorted bucket is empty

        |              |        |              |
        |   Unsorted   |        |    sorted    |
        |              |        |              |
        |              |        |     3,4,5    |
         --------------          --------------

        Finally you have the sorted array.

        Learn More Here - https://en.wikipedia.org/wiki/Selection_sort
        """
        print_msg_box(message)

class string_algorithms:

    def isUnique(self,input_string,hint=False):
        mapp = []
        for i in input_string:
            if i not in mapp:
                mapp.append(i)
        if(hint == True):
            self.isUnique_hint()
        return len(mapp) == len(input_string)

    def isUnique_hint(self):
        message ="""
        Unique Character Checking
        ------------------------------------

        Purpose : checking if all the characters in a given string are unique
        Method : list comprehension

        Time Complexity: Worst Case - O(n), n = length of the input string

        Hint :
        How about using the inbuilt list data structure ?

        Pseudocode:
        --> create an empty list named mapp
        --> for i in input string
                if i not in mapp
                    add i to the empty list
        --> The string is unique only when the
            length of the map after the total
            iterations is same as that of the
            length of the input string

        Visualization:

        Given String :

        "aabcc"

        Empty List:

         ----------------
        |                |
         ----------------

        after first iteration :

         ----------------
        |       a        |
         ----------------

        after second iteration :

         ----------------
        |       a        |
         ----------------

        [because a was already in the list]

        after third iteration :

         ----------------
        |      a b       |
         ----------------

        Finally :

         ----------------
        |     a b c      |    size = 3 which is not equal to length of "aabcc"
         ----------------

        Learn More about Lists Here - https://docs.python.org/3/tutorial/datastructures.html
        """
        print_msg_box(message)


    def isPermutation(self,input1,input2):
        mapp1 = []
        mapp2 = []
        for i in input1:
            if i not in mapp1:
                mapp1.append(i)
        for j in input2:
            if j not in mapp2:
                mapp2.append(j)
        mapp1.sort()
        mapp2.sort()
        return mapp1==mapp2

    def URLify(self,input_str,key):
        input2 = ""
        for i in range(len(input_str)):
            if(input_str[i] != ' '):
                input2+=input_str[i]
            elif((input_str[i]==' ') and (input_str[i+1] == ' ')):
                return input2
            elif((input_str[i]==' ') and (input_str[i+1] != ' ')):
                input2 += key
        return input2

    def isPalindromicPermutation(self,input1):
        mapp = {}
        for i in range(len(input1)):
            key = input1[i]
            if(key in mapp.keys()):
                mapp[key] += 1
            else:
                mapp.update({key:1})
        flag = 0
        for i in mapp.keys():
            if(mapp[i] %2 == 1):
                flag+=1
        return flag<=1

    def oneEditAwayInsert(self,input1,input2):
        index1 = 0
        index2 = 0
        while((index2 < len(input2)) and (index1 < len(input1))):
            if(input1[index1] != input2[index2]):
                if(index1 != index2):
                    return False
                index2+=1
            else:
                index1+=1
                index2+=1
        return True

    def oneEditAwayReplace(self,input1,input2):
        flag = False
        for i in range(len(input1)):
            if(input2[i]!=input1[i]):
                if(flag):
                    return False
                flag = True
        return True

    def oneEditAway(self,input1,input2):
        if(len(input1)==len(input2)):
            return self.oneEditAwayReplace(input1,input2)
        elif(len(input1)+1==len(input2)):
            return self.oneEditAwayInsert(input1,input2)
        elif(len(input1)-1==len(input2)):
            return self.oneEditAwayInsert(input2,input1)
        return False

    def compressedString(self,input1):
        mapp = {}
        output = ""
        for i in range(len(input1)):
            key = input1[i]
            if(key in mapp.keys()):
                mapp[key]+=1
            else:
                mapp.update({key:1})
        for key in mapp.keys():
            output = output + key + str(mapp[key])
        if(len(output) <= len(input1)):
            return output
        else:
            return input1

    def rotateImage(self,img_arr,n):
        for layer in range(int(n/2)):
            first = layer
            last = n-1-layer
            for i in range(first,last):
                offset = i - first
                top = img_arr[first][i]
                img_arr[first][i] = img_arr[last - offset][first]
                img_arr[last - offset][first] = img_arr[last][last - offset]
                img_arr[last][last - offset] = img_arr[i][last]
                img_arr[i][last] = top

s = string_algorithms()
a = s.isUnique("aabbccdd",True)
