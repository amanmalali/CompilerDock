**Code Compiler**
----
Compiles the code sent to the URL and returns the output in JSON format

* **URL**
   
   /

* **Method:**
   
   POST
  
*  **URL Params**
   
   `None`


* **Data Params**
   
   **Required:**
    *  lang=[string]
     * code=[string]
     * id=[string]
    
  **Optional:**
    * stdin=[string]


* **Success Response:**
  * **Code:** 200
  *  **Content:** 
        ```json
        {
            "output": "Hello World\n",
            "error": 0,
            "fail": 0,
            "timeout": 0,
            "id": 1
        }
        ```
 

* **Sample Call:**
    ```json
    {
        "lang": "python3",
        "code": "print('Hello World')",
        "id": "1",
        "stdin": ""
  }  
