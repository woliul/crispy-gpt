## **180-Day Python Learning Plan**

***Note: Learning and Practice Separated***

**Schedule:**

- **9:00 - 10:00 PM:** Learning (detailed lectures and concepts).
- **10:00 - 11:30 PM:** Practice (coding exercises, examples, and mini-projects).

**Note:** Every Friday is a reflection day.

---

### **Day 2: Variables and Data Types**

**Learning (9:00 - 10:00 PM)**  
Today we’ll cover:

1. **Variables:** What they are and how to create them.
2. **Data types:** Strings, integers, floats, and basic type conversions.

---

### **1. What is a Variable?**

A variable is a named container that stores a value. Think of it as a "box" where you can store data.

- You can name a variable with letters, numbers, and underscores (`_`).
- Example:
  ```
  name = "Alice"
  age = 25
  height = 5.7
  ```  
  In the above example:
   - `name` holds a string (`"Alice"`)
   - `age` holds an integer (`25`)
   - `height` holds a float (`5.7`)

---

### **2. Common Data Types in Python**

1. **String (`str`):**  
   Text enclosed in quotes.  
   Example: `"Hello, world!"`
   ```
   greeting = "Hello, world!"
   print(greeting)
   ```  

2. **Integer (`int`):**  
   Whole numbers (positive or negative).  
   Example: `42`
   ```
   number = 42
   print(number)
   ```

3. **Float (`float`):**  
   Decimal numbers.  
   Example: `3.14`
   ```
   pi = 3.14
   print(pi)
   ```

4. **Boolean (`bool`):**  
   `True` or `False`.
   ```
   is_sunny = True
   print(is_sunny)
   ```

---

### **3. Type Conversion (Casting)**

You can convert one type to another using `int()`, `float()`, `str()`, etc.  
Examples:

```
age = "30"  # This is a string
age_as_int = int(age)  # Converts to integer
print(age_as_int)
```  

```
number = 42  # Integer
number_as_str = str(number)  # Converts to string
print(number_as_str)
```

---

### **Practice Exercises (10:00 - 11:30 PM)**

1. **Exercise 1:** Create and print variables of different types:
   - A string variable holding your name.
   - An integer variable for your age.
   - A float variable for your height.
   - A boolean variable indicating if you like pizza.  
     Example:
   ```
   name = "John"
   age = 28
   height = 5.9
   likes_pizza = True
   print(name, age, height, likes_pizza)
   ```

2. **Exercise 2:** Use type conversion to do the following:
   - Convert a float to an integer.
   - Convert an integer to a string and print it.  
     Example:
   ```
   number = 3.75
   number_as_int = int(number)
   print(number_as_int)  # Output: 3
   ```

3. **Exercise 3:** Create a program that asks the user for their name and age, then prints a message like:  
   `"Hello, [name]! You are [age] years old."`  
   Example:
   ```
   name = input("Enter your name: ")
   age = input("Enter your age: ")
   print(f"Hello, {name}! You are {age} years old.")
   ```

---

Let me know when you’re done, or if you have any questions while practicing! 😊