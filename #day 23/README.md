# 📘 XML & XSD Example – Employee Data

## 🧩 Overview
This project demonstrates the use of **XML (Extensible Markup Language)** and **XSD (XML Schema Definition)** to define and validate structured data.  
In this example, we describe a list of **employees**, each having personal information such as name, age, gender, phone, and address.

---

## 📂 What I Learned Today
In today’s class, I learned:
- What XML is and how it is used to store and transport data.
- How XSD (Schema) defines the structure and data type rules for an XML document.
- The relationship between XML and its corresponding XSD file.
- How to use namespaces and schema validation attributes.

---

## 🧾 XML Description
The **XML file** (`employee.xml`) contains multiple `<employee>` elements inside the main `<employees>` root element.  
Each employee includes details such as name, age, gender, phone, and address, along with an attribute called `status`.

### 📄 Sample XML:
```xml
<employees xmlns="http://www.example.com/employee"
    xmlns:xsi="http://www.example.com/2025/XMLSchema-instance"
    xsi:schemaLocation="http://www.example.com/employee employee.xsd">

    <employee status="active">
        <name>Rahul</name>
        <age>25</age>
        <gender>Male</gender>
        <phone>4223352345</phone>
        <address>61, North Campus, Hyderabad, India</address>
    </employee>

    <employee status="inactive">
        <name>Prince</name>
        <age>25</age>
        <gender>Male</gender>
        <phone>4222452345</phone>
        <address>61, North Campus, Gujarat, India</address>
    </employee>
</employees>
