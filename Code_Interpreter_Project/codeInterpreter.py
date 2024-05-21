import subprocess

def runCode(code, test_code=False):
    """
    This function takes a string of code and executes it in a separate process.
    If test_code is True, it will not return the code to the user unless it runs without errors.
    It returns the output of the code execution or the error if one occurs,
    along with a user-friendly explanation and a suggestion for improvement.
    """
    try:
        # Execute the code as a separate process
        result = subprocess.run(['python', '-c', code], capture_output=True, text=True, check=True)
        # Return the successful output
        return "Code executed successfully:\n" + result.stdout, None
    except subprocess.CalledProcessError as e:
        # If test_code is True, do not return the code to the user
        if test_code:
            return None, f"An error occurred while testing the improved code:\n{e.stderr}"
        else:
            # Format the error message for the user
            error_message = f"An error occurred in your code:\n{e.stderr}"
            # Return the error message and suggestion
            return error_message, code