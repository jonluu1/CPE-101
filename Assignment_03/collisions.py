import data
import vector_math as vm

def sphere_intersection_point(ray, sphere):
    a = vm.dot_vector(ray.dir, ray.dir)
    b = vm.dot_vector(vm.scale_vector(vm.vector_from_to(sphere.center, ray.pt), 2), ray.dir)
    c = vm.dot_vector(vm.vector_from_to(sphere.center, ray.pt), vm.vector_from_to(sphere.center, ray.pt)) - sphere.radius ** 2
    x = vm.quadForm(a, b, c)

    # pt_center_vec = vm.vector_from_to(sphere.center, ray.pt)
    # a = vm.dot_vector(ray.dir, ray.dir)
    # b = vm.dot_vector(vm.scale_vector(pt_center_vec, 2), ray.dir)
    # c = vm.dot_vector(pt_center_vec, pt_center_vec) - sphere.radius ** 2
    # x = vm.quadForm(a, b, c)

    def point_along_ray(ray, t):
        if t >= 0:
            x = ray.pt.x + ray.dir.x * t
            y = ray.pt.y + ray.dir.y * t
            z = ray.pt.z + ray.dir.z * t
            return data.Point(x, y, z)
        else:
            return None

    if x is None:
        return None
    if isinstance(x, list):
        intersections = []
        for i in x:
            intersections.append(point_along_ray(ray, i))

        distances = []
        for i in intersections:
            if i is not None:
                distances.append(vm.distForm(i, ray.pt))
            else:
                distances.append(None)


        if distances[0] is None:
            return intersections[1]
        if distances[1] is None:
            return intersections[0]
        if distances[0] < distances[1]:
            return intersections[0]
        else:
            return intersections[1]
    else:
        intersection = point_along_ray(ray, x)
        return intersection





def find_intersection_points(sphere_list, ray):
    intersectionNoneList = []
    for i in sphere_list:
        intersectionNoneList.append(sphere_intersection_point(ray, i))
    intersectionList = []
    for i in intersectionNoneList:
        if i is not None:
            intersectionList.append(i)
    return intersectionList

    # intersections_and_none = map(lambda sphere: (sphere, sphere_intersection_point(ray, sphere)), sphere_list)
    # return filter(lambda intersections: intersections[1] is not None, intersections_and_none)
