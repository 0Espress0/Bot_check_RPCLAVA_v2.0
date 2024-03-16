# Bot_check_RPCLAVA_v2.0
1. การอ่านไฟล์ RPC Endpoint: โค้ดจะอ่าน URL ของ RPC Endpoint จากไฟล์ที่ระบุ (rpc_endpoint_file) และเชื่อมต่อกับโหนด Ethereum ผ่าน URL ดังกล่าว.
2. การอ่านไฟล์ Private Key: โค้ดจะอ่าน private key ของวอลเล็ตจากไฟล์ที่ระบุ (private_key_file) เพื่อใช้ในการเชื่อมต่อกับโหนด Ethereum และเปิดใช้งานวอลเล็ต.
3. การเชื่อมต่อกับโหนด Ethereum: โค้ดจะใช้ URL ของ RPC Endpoint เพื่อเชื่อมต่อกับโหนด Ethereum โดยใช้ไลบรารี Web3.
4. การเปิด/ปิดการใช้งานวอลเล็ต: โค้ดจะใช้ private key เพื่อเปิดหรือปิดการใช้งานวอลเล็ตบนโหนด Ethereum โดยใช้บัญชีที่สร้างจาก private key นั้น.
5. การตรวจสอบสถานะของโหนด Ethereum: โค้ดจะตรวจสอบสถานะของโหนด Ethereum เช่น การซิงโครไนซ์ และแสดงผลข้อมูลนี้ที่หน้าจอ.
6. การตรวจสอบยอดคงเหลือในวอลเล็ต: โค้ดจะตรวจสอบยอดคงเหลือในวอลเล็ตที่เกี่ยวข้องกับ private key ที่กำหนด และแสดงผลข้อมูลนี้ที่หน้าจอ.
7. การทำงานแบบวนรอบ: โค้ดจะทำงานแบบวนรอบโดยรอบทุก ๆ 10 วินาทีเพื่อตรวจสอบสถานะของโหนดและยอดคงเหลือในวอลเล็ต.
--------------------------------------------------
เตรียมความพร้อม
1. ติดตั้ง Python version 3 ขึ้นไป
2. ติดตั้ง Module Web3 >>command : pip3 install web3
   
   2.1. sudo apt update
   2.2. sudo apt install python3 -y
   2.3. pip3  install numpy
   2.4. sudo apt install python3-pip -y
   2.5. pip install web3

ขั้นตอนการใช้งาน
1. ทำการเพ่ิม RPC LAVA ของตัวเองในไฟล์ rpc_endpoint.txt
2. ทำการเพิ่ม Private kry wallet (EVM Chain) ไปที่ไฟล์ private_key.txt
3. หลักจากติดตั้งเรียบร้อยให้ทำการรัน command >>python3 Bot_LAVA_PKWv2.py
*** ไฟล์ ฺBot_LAVA_PKWv2.py, private_key.txt & rpc_endpoint.txt จะต้องอยู่ใน folder เดียวกัน ***

⚠️⚠️⚠️ Code นี้มีการใช้งาน Private key wallet โปรดใช้ด้วยความระมันระวัง ⚠️⚠️⚠️
