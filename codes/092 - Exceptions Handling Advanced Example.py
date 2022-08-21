'''
====================================
-- 092 - Exceptions Handling Advanced Example 
-- link : https://www.youtube.com/watch?v=RjkKwZ-p7YU&list=PLDoPjvoNmBAyE_gei5d18qkfIe-Z8mocs 
====================================
'''
# -----------------------------------
# --      Exceptions Handling      --
# -- Try | Except | Else | Finally --
# --       Advanced Example        --
# -----------------------------------

the_file = None

the_tries = 5

while the_tries &gt; 0:

  try:  # Try To Open The File

    print("Enter The File Name With Absolute Path To Open")

    print(f"You Have {the_tries} Tries Left")

    print("Example: D:\Python\Files\yourfile.extension")

    file_name_and_path = input("File Name =&gt; : ").strip()

    the_file = open(file_name_and_path, 'r')

    print(the_file.read())

    break

  except FileNotFoundError:

    print("File Not Found Please Be Sure The Name is Valid")

    the_tries -= 1

  except:

    print("Error Happen")

  finally:

    if the_file is not None:

      the_file.close()

      print("File Closed.")

else:

  print("All Tries Is Done")