
from writing_tensile_utils import *
import os
import sys


def generate_csv_file(filename, results):
    """
    Write material strength results to a CSV file.
    """

    # Step 1: store the output filename
    output_file_name = filename

    # Step 2: open the file in write mode
    with open(output_file_name, "w") as file:

        # Step 3: write the CSV header
        file_header = (
            "Sample_Name,Material_Type,Tensile_Strength,"
            "Fracture_Strain,Elastic_Modulus,Yield_Strength\n"
        )
        file.write(file_header)

        # Step 4: iterate through the results
        for r in results:
            name = r.name
            material_type = r.material_type
            tensile_strength = r.tensile_strength
            fracture_strain = r.fracture_strain
            modulus = r.elastic_modulus
            yield_strength = r.yield_strength

            # Step 5: combine the values into one CSV row
            string_to_write = (
                str(name) + ","
                + str(material_type) + ","
                + str(tensile_strength) + ","
                + str(fracture_strain) + ","
                + str(modulus) + ","
                + str(yield_strength) + "\n"
            )

            file.write(string_to_write)

    return True


if __name__ == "__main__":

    # Get the path to the data folder
    path_to_tensile_folder = "../../../data/tensile/"

    # Check that the input folder exists
    if not os.path.isdir(path_to_tensile_folder):
        print("Error: Tensile data folder not found:", os.path.abspath(path_to_tensile_folder))
        sys.exit(-1)

    # List to hold all sample results
    results = []

    # Each folder in data/ is a different material
    materials = []

    for root, dirs, files in os.walk(path_to_tensile_folder):
        materials.extend(dirs)
        break

    # Walk through each material folder and file
    for material in materials:
        print("Parsing material:", material)

        path_to_material_folder = os.path.join(
            path_to_tensile_folder, material
        )

        for root, dirs, files in os.walk(path_to_material_folder):

            # Parse each CSV file
            for file_name in files:

                if not file_name.lower().endswith(".csv"):
                    continue

                print("\tLoad sample:", file_name)

                # Create the path to the sample file
                path_to_sample = os.path.join(root, file_name)

                # Parse the sample data
                sample_diameter, time, displacement, force, strain = (
                    parse_tensile_file(path_to_sample)
                )

                # Calculate stress
                stress = calculate_stress(force, sample_diameter)

                if stress is None:
                    print(
                        "Error! No stress returned. Check calculate_stress() "
                        "in writing_tensile_utils.py."
                    )
                    sys.exit(-1)

                # Calculate tensile strength and fracture strain
                ultimate_tensile_strength, fracture_strain = (
                    calculate_max_strength_strain(strain, stress)
                )

                if ultimate_tensile_strength == -1 or fracture_strain == -1:
                    print(
                        "Error! Tensile strength or fracture strain calculation failed."
                    )
                    sys.exit(-1)

                # Calculate elastic modulus
                linear_index, slope, intercept = calculate_elastic_modulus(
                    strain, stress
                )

                if slope is None:
                    print(
                        "Error! Elastic modulus calculation failed. "
                        "Check calculate_elastic_modulus() in writing_tensile_utils.py."
                    )
                    sys.exit(-1)

                elastic_modulus = slope / 1000

                # Calculate yield strength
                yield_strength = calculate_yield_strength(
                    strain, stress, slope
                )

                if yield_strength == -1:
                    print(
                        "Error! Yield strength calculation failed. "
                        "Check calculate_percent_offset() in writing_tensile_utils.py."
                    )
                    sys.exit(-1)

                # Create a material sample
                sample = MaterialSample()
                sample.name = os.path.splitext(file_name)[0]
                sample.material_type = material
                sample.tensile_strength = ultimate_tensile_strength
                sample.fracture_strain = fracture_strain
                sample.elastic_modulus = elastic_modulus
                sample.yield_strength = yield_strength

                # Add the sample to the results list
                results.append(sample)

    # Print results for inspection
    for r in results:
        print("Sample Name:", r.name)
        print("\tMaterial Type:", r.material_type)
        print("\tTensile Strength:", r.tensile_strength)
        print("\tFracture Strain:", r.fracture_strain)
        print("\tElastic Modulus:", r.elastic_modulus)
        print("\tYield Strength:", r.yield_strength)

    # Write the results to a CSV file
    generate_csv_file("tensile_data_student.csv", results)

    print("Done!")
