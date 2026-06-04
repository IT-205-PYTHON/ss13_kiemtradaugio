list_staff = []
while True :
    print("="*50)
    print("         QUẢN LÝ NHÂN SỰ - STAFF MANAGER         ")
    print("="*50)
    print('''
    1. Thêm nhân viên mới 
    2. Danh sách nhân viên
    3. Xoá nhân viên khỏi hệ thống
    4. Thoát chương trình
    ''')
    print("="*50)
    select =input("Nhập vào lựa chọn của bạn: ")
    match select:
        case '1':
            while True:
                new_id = 101 if not list_staff else (max(staff["id"] for staff in list_staff) + 1 )
                new_staff= input("Nhập vào tên nhân viên: ").strip()
                if new_staff == "":
                    print("Tên không được để trống , Vui lòng nhập lại")
                    continue

                salary = input('Nhập vào mức lương: ').strip()
                if salary == "":
                    print("Tên không được để trống , Vui lòng nhập lại")
                    continue
                elif not salary.isdigit() :
                    print("Vui lòng chỉ nhập số nguyên , vui lòng nhập lại")
                    continue
                elif int(salary) < 0 :
                    print("Mức lương phải lớn hơn 0 , vui lòng nhập lại")
                    continue
                new_dict = {
                    "id":new_id,
                    "name_staff":new_staff,
                    "salary":salary}
                list_staff.append(new_dict)
                print(list_staff)
                print(f"Thông báo: \"Thêm nhân viên thành công ! ID: {new_id}\" ")
                break
        


        case '2':
            if len(list_staff) == 0 :
                print("Chưa có dữ liệu nhân sự!")
            else:
                print(
                    f"{'ID':<8}  |"
                    f"{'  TÊN NHÂN VIÊN':<20}  |"
                    f"{'  MỨC LƯƠNG':<13}"
                )
                print("-"*50)
                for staff in list_staff:
                    print(
                        f"{ staff["id"]:<8}  |"
                        f" { staff["name_staff"]:<20} |"
                        f" { staff["salary"]:<13}"
                    )
        case '3':
            while True:
                check_id = input("Nhập vào ID cần xoá: ").strip()
                if not check_id.isdigit():
                    print("Vui lòng chỉ nhập số , vui lòng nhập lại")
                    continue
                elif check_id == "":
                    print("Không được bỏ trống ID , vui lòng nhập lại")
                    continue
                int_id = int(check_id)
                is_check_id = False
                for i , staff in enumerate(list_staff):
                    if int_id == staff["id"] :
                        delete_id = list_staff.pop(i)["id"]
                        
                        is_check_id = True
                        break

                if is_check_id :
                    print(f"Đã xóa nhân viên ID {delete_id} thành công!")
                else: 
                    print("Không tìm thấy ID nhân viên để xoá")
                break
                
        case '4':
            print("Cảm ơn bạn đã sử dụng chương trình !!")
            break
        case _ :
            print("Bạn đã nhập sai yêu cầu , vui lòng nhập lại")
            continue
            