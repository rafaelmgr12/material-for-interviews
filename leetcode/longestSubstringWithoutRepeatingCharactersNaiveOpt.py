def min_sub_array_len_verbose(target, nums):
    n = len(nums)
    min_length = float('inf')
    left = 0
    sum = 0
    
    for right in range(n):
        sum += nums[right]
        print(f"Adicionando {nums[right]}, nova soma = {sum}")
        
        while sum >= target:
            min_length = min(min_length, right - left + 1)
            print(f"Soma >= target, tentando contrair a janela: subarray = {nums[left:right+1]}, comprimento = {right - left + 1}")
            sum -= nums[left]
            left += 1
            print(f"Janela contraída, nova soma = {sum}, nova janela começa em {left}")
            
    return min_length if min_length != float('inf') else 0

# Testando a função com o exemplo dado e prints
target = 7
nums = [2,3,1,2,4,3]
min_sub_array_len_verbose(target, nums)
