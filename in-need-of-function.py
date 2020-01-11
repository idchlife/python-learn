import inspect

def please_reverse_array(reverse_function):
  assert inspect.isfunction(reverse_function), f"What you passed is not a function, it's: {type(reverse_function)}"

  original = [1, 4, 6, 22, 10]

  reversed = reverse_function(original)

  assert reversed == original.reverse(), f"Uh-oh, it seems your reverse function is not working properly... Got: {reversed}"

  print("Hooray! Task for reverse function is complete!")


please_reverse_array(your_function)
