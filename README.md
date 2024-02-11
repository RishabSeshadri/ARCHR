# ARCHR
### Proximity-based authentication made easy
#### Rishab Seshadri, Carlos DeSantiago
------------------------------------------------------------------

With credit card scams and skimmers on the rise, this kind of information-based theft becomes a more pressing issue. Card cloning gives criminals the ability to use replica cards to withdraw large amounts of cash from ATMs. With the help of ARCHR's use of Bluetooth Low Energy (BLE) technology, companies will be able to implement ARCHR into their ATMs to give customers the ability to connect their phones to their bank accounts as a means of authentication.

### How does it work?
ARCHR uses BLE to track registered devices that are within a short range of the hosting device (i.e., the ATM). When a recognized device enters the range, ARCHR allows the associated account to make transactions at the location, in pair with the already existing debit or credit card. This allows for a smooth, automatic authentication process that combats scammers who use replica cards with cloned data, without requiring the customer to even take their phone out of their pocket. If a purchase is flagged without the approved device in range, ARCHR automatically marks the account as compromised.

### Demo
Obviously, we are not able to demonstrate ARCHR's full potential using an ATM at this moment. However, we have developed a simple user interface that demonstrates ARCHR's technology by allowing you to register a sample device, using 'nRF Connect' (the "phone"), to our database and verify its location from a sample source such as a laptop (the "ATM"). 

### Limitations
As mentioned before, we do not have an ATM to display ARCHR's work on. Additionally, due to the paywall of Apple's developer account and the lack of need for a custom app, we chose to use 'nRF Connect' to simulate a BLE-advertising device. However, ARCHR can easily be implemented into a pre-existing banking app by advertising the device using BLE when a device is within a certain latitude, longitude, and altitude of the ATM.