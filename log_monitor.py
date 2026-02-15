def analyze_logs(file_path):
    errors = []
    warnings = []

    with open(file_path, "r") as file:
        for line in file:
            if "ERROR" in line:
                errors.append(line.strip())
            elif "WARNING" in line:
                warnings.append(line.strip())

    return errors, warnings


errors, warnings = analyze_logs("sample.log")

print("\nErrors found:")
for error in errors:
    print("-", error)

print("\nWarnings found:")
for warning in warnings:
    print("-", warning)
