from tkinter import *
from datetime import datetime


# Read 5 letters word dictionary:
file_handler = open("5LW.txt", "r")
word_list =  file_handler.read().splitlines()
file_handler.close()

# Define GUI Frames:
root = Tk()
root.title("Woordle finder (5 letters only)")
perfect_entries_frame = Frame(root)
perfect_entries_frame.grid(row=2, column=1)

# Good entries:
def validate_entries(P):
    # Validation function for perfect entries (one single letter, no more)
    if len(P) >= 0 and P.isalpha():
        # empty Entry is ok
        return True
    else:
        # Anything else, reject it
        return False

vcmd_entries = (root.register(validate_entries), '%P')

good_entries_label = Label(root, text="Enter good, confirmed letters: ", anchor="e", width=30)
good_entries_label.grid(row=0, column=0)
good_entries = Entry(root, width=15, font=15, bd=10, bg="#FEFED3", validate="key", validatecommand=vcmd_entries)
good_entries.grid(row=0, column=1)

# Bad entries:
bad_entries_label = Label(root, text="Enter bad, confirmed letters: ", anchor="e", width=30)
bad_entries_label.grid(row=1, column=0)
bad_entries = Entry(root, width=15, font=15, bd=10, bg="#FA6E55", validate="key", validatecommand=vcmd_entries)
bad_entries.grid(row=1, column=1)

# Perfect entries:
def validate_perf_entries(P):
    # Validation function for perfect entries (one single letter, no more)
    if len(P) == 0:
        # empty Entry is ok
        return True
    elif len(P) == 1 and P.isalpha():
        # Entry with 1 digit is ok
        return True
    else:
        # Anything else, reject it
        return False

vcmd_perf_entries = (root.register(validate_perf_entries), '%P')

perfect_entries_label = Label(root, text="Enter known position entries, leave empty for unknown: ", anchor="e", width=30, wraplength=200)
perfect_entries_label.grid(row=2, column=0)
perfect_entries1 = Entry(perfect_entries_frame, width=2, font=15, bd=7, bg="#5CFC51", validate="key", validatecommand=vcmd_perf_entries)
perfect_entries1.grid(row=0, column=0, sticky="w")
# perfect_entries1.insert(0, "?")
#
perfect_entries2 = Entry(perfect_entries_frame, width=2, font=15, bd=7, bg="#5CFC51", validate="key", validatecommand=vcmd_perf_entries)
perfect_entries2.grid(row=0, column=1, sticky="w")
# perfect_entries2.insert(0, "?")
#
perfect_entries3 = Entry(perfect_entries_frame, width=2, font=15, bd=7, bg="#5CFC51", validate="key", validatecommand=vcmd_perf_entries)
perfect_entries3.grid(row=0, column=2, sticky="w")
# perfect_entries3.insert(0, "?")
#
perfect_entries4 = Entry(perfect_entries_frame, width=2, font=15, bd=7, bg="#5CFC51", validate="key", validatecommand=vcmd_perf_entries)
perfect_entries4.grid(row=0, column=3, sticky="w")
# perfect_entries4.insert(0, "?")
#
perfect_entries5 = Entry(perfect_entries_frame, width=2, font=15, bd=7, bg="#5CFC51", validate="key", validatecommand=vcmd_perf_entries)
perfect_entries5.grid(row=0, column=4, sticky="w")
# perfect_entries5.insert(0, "?")

# Solutions text
solution = Label(root, bg = "#5CFC51", wraplength=500)
solution.grid(row=4, column=0, columnspan=2)

# "See options" button:
def narrow_options(dictionary, solution_label):
    good_letters = good_entries.get().upper()
    bad_letters = bad_entries.get().upper()
    perf_letter1 = perfect_entries1.get().upper()
    perf_letter2 = perfect_entries2.get().upper()
    perf_letter3 = perfect_entries3.get().upper()
    perf_letter4 = perfect_entries4.get().upper()
    perf_letter5 = perfect_entries5.get().upper()
    # condtioning:
    candidate_words = []
    for item in dictionary:
        # perfect_letters:
        perf_letters_match = True
        if perf_letter1.isalpha():
            if perf_letter1 != item[0]:
                perf_letter_match = False
                continue
        if perf_letter2.isalpha():
            if perf_letter2 != item[1]:
                perf_letter_match = False
                continue
        if perf_letter3.isalpha():
            if perf_letter3 != item[2]:
                perf_letter_match = False
                continue
        if perf_letter4.isalpha():
            if perf_letter4 != item[3]:
                perf_letter_match = False
                continue
        if perf_letter5.isalpha():
            if perf_letter5 != item[4]:
                perf_letter_match = False
                continue
        # good letters:
        contains_good_letters = True
        for good_letter in good_letters:
            if good_letter not in item:
                contains_good_letters = False
                continue
        # bad letters:
        contains_bad_letters = False
        for bad_letter in bad_letters:
            if bad_letter in item:
                contains_bad_letters = True
                continue
        # Final condition:
        if contains_good_letters and (not contains_bad_letters) and perf_letters_match:
            candidate_words.append(item)
        # Update solution:
        # Solutions text
        solution_label['text'] = f"Try out: {candidate_words}"

go_button = Button(root, font=15, text="See options", command=lambda: narrow_options(dictionary=word_list, solution_label=solution))
go_button.grid(row=3, column=0, columnspan=2)

root.mainloop()
