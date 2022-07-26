# I cannot connect my device


## Introduction

::: tip Bootstrap Server:
Bootstrap Server is a process that allows the router to acquire certificates and keys, which are mandatory to step into the process of connecting to the Management Server.
:::

We consider 3 different scenarios:

### **Scenario 1:**
The router is without an internet connection because it is stuck in the permanent Bootstrap Server process and not receiving any successful response from the server. This could happen while the router was in the manufacturing process; it was not loaded into **DMP**.

**Solution:** In this case, the customer needs to contact **[DMP support](mailto:wadmp@advantech.com)** and request the creation of the router in the DMP instance.

### **Scenario 2:**
The router can't connect to the Bootstrap Server with the usual catchphrase: **"Connection to Bootstrap Server failed."**

**Reasons and solutions:** 

1. There is a **firewall** in the way, which denies the router from connecting to the endpoint.
2. Wrong **default Bootstrap Server value** on customer's router. Check that your Bootstrap Server configuration matches the public configuration if you connect to the public server. If you are using a private DMP server, ensure that the address is correct and reachable.
3. The router has **no Internet connection**. Check the internet connection of the customer.

### **Scenario 3:**
The router successfully connects to the Bootstrap Server, and the whole Bootstrap Server process will be successful, but it fails to connect to the Management Server.

**Reasons and solutions:**

1. There is a **firewall** in the way. It has **no connection** to the **Internet**.
2. Wrong **time set** on the router. There can be a problem with the **certificate's validity**if the router's time is different from the server's in orders of months or more.

