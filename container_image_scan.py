import argparse
import json
import subprocess

def scan_container_image(image_name, output_file):
    # Call the grype tool to scan the container image
    command = ['grype', image_name, '--json', output_file]
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Check the result of the scan and return an appropriate exit code
    if result.returncode == 0:
        return 0
    else:
        return 1

if __name__ == '__main__':
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Scan container images for vulnerabilities')
    parser.add_argument('--image-name', type=str, help='Name of the container image to be scanned')
    parser.add_argument('--output-file', type=str, help='File where the scan results will be saved')
    args = parser.parse_args()

    # Run the grype tool to scan the container image and save the results to a file
    exit_code = scan_container_image(args.image_name, args.output_file)
    with open(args.output_file, 'r') as f:
        scan_results = json.load(f)

    # Print the scan results and exit with the appropriate exit code
    print(json.dumps(scan_results))
    exit(exit_code)
