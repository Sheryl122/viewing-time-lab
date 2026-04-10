def clean_data(data):
    """
    TODO: Implement your "clean_heartrate_data" function from TLAB #1 & #2
    within this module. Note that this code will be *slightly* different
    from your original function.
    """
    clean_data = []
    
    for row in data:
        if row != 'minutes\n':
            clean_data.append(float(row.strip()))

    return clean_data


sample_list = ['minutes\n', '33.9\n','56.99\n', '38.0\n', '51.22\n', '101.22\n']



control_file = open("data/control.txt")
treatment_file = open("data/treatment.txt")

control_data = control_file.readlines()
treatment_data = treatment_file.readlines()

# TODO: clean both list objects that you created above using the 'clean_data' function
clean_control = clean_data(control_data)
clean_treatment = clean_data(treatment_data)

print("Clean control data: ", clean_control)
print("Clean Treatment data: ", clean_treatment)
