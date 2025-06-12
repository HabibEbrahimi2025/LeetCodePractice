def multiply(num1, num2):
    if num1 == "0" or num2 == "0":
        return "0"

    m, n = len(num1), len(num2)
    result = [0] * (m + n)

    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            mul = int(num1[i]) * int(num2[j])
            sum_ = mul + result[i + j + 1]

            result[i + j + 1] = sum_ % 10
            result[i + j] += sum_ // 10

    # Convert the result array to a string, skipping leading zeros
    result_str = ''.join(map(str, result)).lstrip('0')
    return result_str

# Examples:
print(multiply("123", "456"))  # Output: "56088"
#print(multiply("2", "3"))      # Output: "6"
