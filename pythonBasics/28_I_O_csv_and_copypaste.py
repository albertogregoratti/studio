
import csv
import os
import shutil


file_in = 'C:/Temp/ai_dance2.csv'
folder_out = 'C:/Temp/test_dst/'

def main():
    try:    # if the file does not exist, it would generate an IOError
        # open the file with playlist
        f = open(file_in, 'r')
        csv_reader = (f, delimiter=',')

        pos = 1000
        for row in csv_reader:
            # set song number
            pos = pos + 5
            # get song file full path and title from playlist
            song = row[12]
            # get file extension: last 4 characters
            extension = song[-4:]
            # set new song full title
            new_title = str(pos) + '_' + row[3] + '_' + row[2] + '.' + extension
            # print(new_title)
            # set full path for output file
            file_out = folder_out + new_title
            check_file = os.path.isfile(song)
            if check_file:  # check if the path+file exists
                shutil.copyfile(song, file_out)
                print('Song copied successfully: ' + str(pos) + '_' + row[3])
            else:
                print('Song not found: ' + str(pos) + '_' + row[3])

    except IOError: # this way the script continues with the line after the try/except
        print('Problem opening file \'', file_in, '\'')

    f.close


main()
def find_file(filename, search_path):
   result = []

# Walking top-down from the root
   for root, dir, files in os.walk(search_path):
      if filename in files:
         result.append(os.path.join(root, filename))
   return result

# print(find_file("calls.csv","C:\Temp"))

