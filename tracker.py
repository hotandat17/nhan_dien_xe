import math


class EuclideanDistTracker:
    def __init__(self):
        # Lưu trữ vị trí trung tâm của các đối tượng
        self.center_points = {}
       # Giữ số lượng ID
       # mỗi khi phát hiện id đối tượng mới, số lượng sẽ tăng thêm một
        self.id_count = 0


    def update(self, objects_rect):
        # Hộp và id đối tượng
        objects_bbs_ids = []

        # Lấy điểm trung tâm của đối tượng mới
        for rect in objects_rect:
            x, y, w, h = rect
            cx = (x + x + w) // 2
            cy = (y + y + h) // 2

            # Tìm hiểu xem đối tượng đó đã được phát hiện chưa
            same_object_detected = False
            for id, pt in self.center_points.items():
                dist = math.hypot(cx - pt[0], cy - pt[1])

                if dist < 25:
                    self.center_points[id] = (cx, cy)
                    print(self.center_points)
                    objects_bbs_ids.append([x, y, w, h, id])
                    same_object_detected = True
                    break

            # Đối tượng mới được phát hiện, chúng tôi gán ID cho đối tượng đó
            if same_object_detected is False:
                self.center_points[self.id_count] = (cx, cy)
                objects_bbs_ids.append([x, y, w, h, self.id_count])
                self.id_count += 1

        # Dọn dẹp từ điển theo tâm điểm để loại bỏ các IDS không dùng nữa
        new_center_points = {}
        for obj_bb_id in objects_bbs_ids:
            _, _, _, _, object_id = obj_bb_id
            center = self.center_points[object_id]
            new_center_points[object_id] = center

        # Cập nhật từ điển với các ID không được sử dụng đã bị xóa
        self.center_points = new_center_points.copy()
        return objects_bbs_ids



