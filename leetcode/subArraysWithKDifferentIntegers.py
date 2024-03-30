"""
992. Subarrays with K Different Integers
Hard
Topics
Companies
Given an integer array nums and an integer k, return the number of good subarrays of nums.

A good array is an array where the number of different integers in that array is exactly k.

For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.
A subarray is a contiguous part of an array.

 

Example 1:

Input: nums = [1,2,1,2,3], k = 2
Output: 7
Explanation: Subarrays formed with exactly 2 different integers: [1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2]
Example 2:

Input: nums = [1,2,1,3,4], k = 3
Output: 3
Explanation: Subarrays formed with exactly 3 different integers: [1,2,1,3], [2,1,3], [1,3,4].
 

Constraints:

1 <= nums.length <= 2 * 104
1 <= nums[i], k <= nums.length

"""

class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        # Contador para o número total de subarrays que satisfazem a condição.
        total_subarrays = 0
        
        # Ponteiros para o início e o fim da janela deslizante.
        window_start = 0
        
        # Dicionário para contar a frequência dos elementos na janela.
        element_frequency = {}
        
        # Número de elementos únicos que podemos remover do início da janela
        # sem perder a propriedade de ter exatamente 'k' elementos distintos.
        unique_elements_to_remove = 0
        
        # Iteramos sobre cada elemento do array 'nums'.
        for window_end in range(len(nums)):
            # Adicionamos o elemento atual ao dicionário de frequências.
            current_element = nums[window_end]
            element_frequency[current_element] = element_frequency.get(current_element, 0) + 1
            
            # Se o número de elementos distintos na janela for maior que 'k',
            # precisamos ajustar o início da janela.
            if len(element_frequency) > k:
                # Removemos o elemento do início da janela do dicionário de frequências.
                start_element = nums[window_start]
                element_frequency[start_element] -= 1
                if element_frequency[start_element] == 0:
                    del element_frequency[start_element]
                
                # Ajustamos o início da janela e reiniciamos o contador de elementos únicos removíveis.
                window_start += 1
                unique_elements_to_remove = 0
            
            # Ajustamos o início da janela para incluir apenas subarrays com exatamente 'k' elementos distintos.
            while element_frequency[nums[window_start]] > 1:
                element_frequency[nums[window_start]] -= 1
                window_start += 1
                unique_elements_to_remove += 1
            
            # Se a janela atual tem exatamente 'k' elementos distintos, atualizamos o contador de subarrays válidos.
            if len(element_frequency) == k:
                total_subarrays += 1 + unique_elements_to_remove
        
        return total_subarrays

    
            
    
    def subarraysWithKDistinctnNaiveSolution(self, nums: List[int], k: int) -> int:
        count = 0

        for right in range(len(nums)):
            freq = {}
            for left in range(right, len(nums)):
                freq[nums[left]] = freq.get(nums[left], 0) + 1
                if len(freq) == k:
                    count += 1
                elif len(freq) > k:
                    break

        return count