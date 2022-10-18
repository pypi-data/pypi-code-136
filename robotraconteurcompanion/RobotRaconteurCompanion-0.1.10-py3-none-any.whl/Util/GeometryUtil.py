import RobotRaconteur as RR
RRN = RR.RobotRaconteurNode.s
import numpy as np
import general_robotics_toolbox as rox
from .IdentifierUtil import IdentifierUtil

def _name_from_identifier(id_):
    if id_ is None:
        return None
    return id_.name

class GeometryUtil(object):
    def __init__(self, node = None, client_obj = None):
        if node is None:
            self._node = RRN
        else:
            self._node = node
        self._client_obj = client_obj

        self._vector2_type = self._create_dtypes("Vector2")
        self._vector3_type = self._create_dtypes("Vector3")
        self._vector6_type = self._create_dtypes("Vector6")
        self._point2d_type = self._create_dtypes("Point2D")
        self._point_type = self._create_dtypes("Point")
        self._size2d_type = self._create_dtypes("Size2D")
        self._size_type = self._create_dtypes("Size")
        self._quaternion_type = self._create_dtypes("Quaternion")
        self._transform_type = self._create_dtypes("Transform")
        self._named_transform_type = self._create_structtypes("NamedTransform")
        self._pose_type = self._create_dtypes("Pose")
        self._named_pose_type = self._create_structtypes("NamedPose")
        self._spatial_velocity_type = self._create_dtypes("SpatialVelocity")
        self._spatial_acceleration_type = self._create_dtypes("SpatialAcceleration")
        self._wrench_type = self._create_dtypes("Wrench")

        self._ident_util = IdentifierUtil(self._node, self._client_obj)

    def _create_dtypes(self, type_name):
        try:
            d_type = self._node.GetNamedArrayDType(f"com.robotraconteur.geometry.{type_name}",self._client_obj)
        except:
            d_type = None
        try:
            f_type = self._node.GetNamedArrayDType(f"com.robotraconteur.geometryf.{type_name}",self._client_obj)
        except:
            f_type = None
        try:
            i_type = self._node.GetNamedArrayDType(f"com.robotraconteur.geometryi.{type_name}",self._client_obj)
        except:
            i_type = None

        assert any((d_type, f_type, i_type)), "No geometry service types registered"
        return d_type, f_type, i_type




    def _create_structtypes(self, type_name):
        try:
            d_type = self._node.GetStructureType(f"com.robotraconteur.geometry.{type_name}",self._client_obj)
        except:
            d_type = None
        try:
            f_type = self._node.GetStructureType(f"com.robotraconteur.geometryf.{type_name}",self._client_obj)
        except:
            f_type = None
        try:
            i_type = self._node.GetStructureType(f"com.robotraconteur.geometryi.{type_name}",self._client_obj)
        except:
            i_type = None
        
        assert any((d_type, f_type, i_type)), "No geometry service types registered"
        return d_type, f_type, i_type

    def _create_return_np(self, rr_dtypes, dtype):
        if dtype == np.float64:
            assert rr_dtypes[0], "com.robotraconteur.geometry not registered"
            return np.zeros((1,),dtype=rr_dtypes[0])
        elif dtype == np.float32:
            assert rr_dtypes[1], "com.robotraconteur.geometryf not registered"
            return np.zeros((1,),dtype=rr_dtypes[1])
        elif dtype == np.int32:
            assert rr_dtypes[2], "com.robotraconteur.geometryi not registered"
            return np.zeros((1,),dtype=rr_dtypes[2])
        else:
            assert False, "Invalid dtype"

    def _create_return_struct(self, rr_struct_types, dtype):
        if dtype == np.float64:
            assert rr_struct_types[0], "com.robotraconteur.geometry not registered"
            return rr_struct_types[0]()
        elif dtype == np.float32:
            assert rr_struct_types[1], "com.robotraconteur.geometryf not registered"
            return rr_struct_types[1]()
        elif dtype == np.int32:
            assert rr_struct_types[2], "com.robotraconteur.geometryi not registered"
            return rr_struct_types[2]()
        else:
            assert False, "Invalid dtype"

    def xy_to_vector2(self, xy, dtype=np.float64):
        ret = self._create_return_np(self._vector2_type, dtype)
        ret[0]["x"] = xy[0]
        ret[0]["y"] = xy[1]
        return ret

    def vector2_to_xy(self, rr_vector2):
        return np.array([rr_vector2[0]["x"], rr_vector2[0]["y"]])

    def xyz_to_vector3(self, xyz, dtype=np.float64):
        ret = self._create_return_np(self._vector3_type, dtype)
        ret[0]["x"] = xyz[0]
        ret[0]["y"] = xyz[1]
        ret[0]["z"] = xyz[2]
        return ret

    def vector3_to_xyz(self, rr_vector3):
        return np.array([rr_vector3[0]["x"], rr_vector3[0]["y"], rr_vector3[0]["z"]])

    def abgxyz_to_vector6(self, abgxyz, dtype=np.float64):
        ret = self._create_return_np(self._vector6_type, dtype)
        ret[0]["alpha"] = abgxyz[0]
        ret[0]["beta"] = abgxyz[1]
        ret[0]["gamma"] = abgxyz[2]
        ret[0]["x"] = abgxyz[3]
        ret[0]["y"] = abgxyz[4]
        ret[0]["z"] = abgxyz[5]
        return ret

    def vector6_to_abgxyz(self, rr_vector6):
        return np.array([rr_vector6[0]["alpha"], rr_vector6[0]["beta"], rr_vector6[0]["gamma"], \
            rr_vector6[0]["x"], rr_vector6[0]["y"], rr_vector6[0]["z"]])

    def xy_to_point2d(self, xy, dtype=np.float64):
        ret = self._create_return_np(self._point2d_type, dtype)
        ret[0]["x"] = xy[0]
        ret[0]["y"] = xy[1]
        return ret

    def point2d_to_xy(self, rr_point2d):
        return np.array([rr_point2d[0]["x"], rr_point2d[0]["y"]])

    def xyz_to_point(self, xyz, dtype=np.float64):
        ret = self._create_return_np(self._point_type, dtype)
        ret[0]["x"] = xyz[0]
        ret[0]["y"] = xyz[1]
        ret[0]["z"] = xyz[2]
        return ret

    def point_to_xyz(self, rr_point):
        return np.array([rr_point[0]["x"], rr_point[0]["y"], rr_point[0]["z"]])


    def wh_to_size2d(self, wh, dtype=np.float64):
        ret = self._create_return_np(self._size2d_type, dtype)
        ret[0]["width"] = wh[0]
        ret[0]["height"] = wh[1]
        return ret

    def size2d_to_wh(self, rr_size2d):
        return np.array([rr_size2d[0]["width"], rr_size2d[0]["height"]])

    def whd_to_size(self, whd, dtype=np.float64):
        ret = self._create_return_np(self._size_type, dtype)
        ret[0]["width"] = whd[0]
        ret[0]["height"] = whd[1]
        ret[0]["depth"] = whd[2]
        return ret

    def size_to_whd(self, rr_size):
        return np.array([rr_size[0]["width"], rr_size[0]["height"], rr_size[0]["depth"]])

    def q_to_quaternion(self, q, dtype=np.float64):
        ret = self._create_return_np(self._quaternion_type, dtype)
        ret[0]["w"] = q[0]
        ret[0]["x"] = q[1]
        ret[0]["y"] = q[2]
        ret[0]["z"] = q[3]
        return ret

    def quaternion_to_q(self, rr_quaternion):
        return np.array([rr_quaternion[0]["w"],rr_quaternion[0]["x"],rr_quaternion[0]["y"],rr_quaternion[0]["z"]])

    def R_to_quaternion(self, R, dtype=np.float64):
        return self.q_to_quaternion(rox.R2q(R), dtype)

    def quaternion_to_R(self, rr_quaternion):
        return rox.q2R(self.quaternion_to_q(rr_quaternion))

    def rpy_to_quaternion(self, rpy, dtype=np.float64):
        return self.q_to_quaternion(rox.R2q(rox.rpy2R(rpy)), dtype)

    def quaternion_to_rpy(self, rr_quaternion):
        return rox.R2rpy(rox.q2R(self.quaternion_to_q(rr_quaternion)))

    def rox_transform_to_transform(self, rox_transform, dtype=np.float64):
        ret = self._create_return_np(self._transform_type, dtype)
        ret[0]["rotation"] = self.R_to_quaternion(rox_transform.R)
        ret[0]["translation"] = self.xyz_to_vector3(rox_transform.p)
        return ret

    def transform_to_rox_transform(self, rr_transform):
        R = self.quaternion_to_R(rr_transform["rotation"])
        p = self.vector3_to_xyz(rr_transform["translation"])
        return rox.Transform(R,p)

    def _xyz_rpy_to_rox_transform(self, xyz,rpy,parent_frame_id=None,child_frame_id=None):
        p = xyz
        R = rox.rpy2R(rpy)
        return rox.Transform(R,p,parent_frame_id,child_frame_id)

    def _rox_transform_to_xyz_rpy(self, rox_transform):
        R = rox_transform.R
        p = rox_transform.p
        return p, rox.R2rpy(R)

    def _rox_transform_to_xyz_rpy_named(self, rox_transform):
        R = rox_transform.R
        p = rox_transform.p
        parent_frame_id = rox_transform.parent_frame_id
        child_frame_id = rox_transform.child_frame_id
        return p, rox.R2rpy(R), parent_frame_id, child_frame_id

    def xyz_rpy_to_transform(self, xyz, rpy, dtype=np.float64):
        return self.rox_transform_to_transform(self._xyz_rpy_to_rox_transform(xyz,rpy),dtype)

    def transform_to_xyz_rpy(self, transform):
        return self._rox_transform_to_xyz_rpy(self.transform_to_rox_transform(transform))

    def rox_transform_to_named_transform(self, rox_transform, dtype=np.float64):
        ret = self._create_return_struct(self._named_transform_type, dtype)
        ret.transform = self.rox_transform_to_transform(rox_transform)
        ret.child_frame = self._ident_util.CreateIdentifierFromName(rox_transform.child_frame_id)
        ret.parent_frame = self._ident_util.CreateIdentifierFromName(rox_transform.parent_frame_id)
        return ret

    def named_transform_to_rox_transform(self, rr_named_transform):
        R = self.quaternion_to_R(rr_named_transform.transform["rotation"])
        p = self.vector3_to_xyz(rr_named_transform.transform["translation"])
        return rox.Transform(R,p, _name_from_identifier(rr_named_transform.parent_frame), \
            _name_from_identifier(rr_named_transform.child_frame))

    def xyz_rpy_to_named_transform(self, xyz, rpy, parent_frame_id, child_frame_id, dtype=np.float64):
        return self.rox_transform_to_named_transform(self._xyz_rpy_to_rox_transform(xyz,rpy,parent_frame_id,child_frame_id),dtype)

    def named_transform_to_xyz_rpy(self, transform):
        return self._rox_transform_to_xyz_rpy_named(self.named_transform_to_rox_transform(transform))

    def rox_transform_to_pose(self, rox_transform, dtype=np.float64):
        ret = self._create_return_np(self._pose_type, dtype)
        ret[0]["orientation"] = self.R_to_quaternion(rox_transform.R)
        ret[0]["position"] = self.xyz_to_point(rox_transform.p)
        return ret

    def pose_to_rox_transform(self, rr_pose):
        R = self.quaternion_to_R(rr_pose["orientation"])
        p = self.vector3_to_xyz(rr_pose["position"])
        return rox.Transform(R,p)

    def xyz_rpy_to_pose(self, xyz, rpy, dtype=np.float64):
        return self.rox_transform_to_pose(self._xyz_rpy_to_rox_transform(xyz,rpy),dtype)

    def pose_to_xyz_rpy(self, transform):
        return self._rox_transform_to_xyz_rpy(self.pose_to_rox_transform(transform))

    def rox_transform_to_named_pose(self, rox_transform, dtype=np.float64):
        ret = self._create_return_struct(self._named_pose_type, dtype)
        ret.pose = self.rox_transform_to_pose(rox_transform)
        ret.frame = self._ident_util.CreateIdentifierFromName(rox_transform.child_frame_id)
        ret.parent_frame = self._ident_util.CreateIdentifierFromName(rox_transform.parent_frame_id)
        return ret

    def named_pose_to_rox_transform(self, rr_named_pose):
        R = self.quaternion_to_R(rr_named_pose.pose["orientation"])
        p = self.vector3_to_xyz(rr_named_pose.pose["position"])
        return rox.Transform(R,p,_name_from_identifier(rr_named_pose.parent_frame), \
            _name_from_identifier(rr_named_pose.frame))

    def xyz_rpy_to_named_pose(self, xyz, rpy, parent_frame_id, child_frame_id, dtype=np.float64):
        return self.rox_transform_to_named_pose(self._xyz_rpy_to_rox_transform(xyz,rpy,parent_frame_id,child_frame_id),dtype)

    def named_pose_to_xyz_rpy(self, transform):
        return self._rox_transform_to_xyz_rpy_named(self.named_pose_to_rox_transform(transform))

    def array_to_spatial_velocity(self, spatial_velocity, dtype=np.float64):
        ret = self._create_return_np(self._spatial_velocity_type, dtype)
        ret[0]["angular"]["x"] = spatial_velocity[0]
        ret[0]["angular"]["y"] = spatial_velocity[1]
        ret[0]["angular"]["z"] = spatial_velocity[2]
        ret[0]["linear"]["x"] = spatial_velocity[3]
        ret[0]["linear"]["y"] = spatial_velocity[4]
        ret[0]["linear"]["z"] = spatial_velocity[5]
        return ret

    def spatial_velocity_to_array(self, rr_spatial_velocity):
        return np.array([rr_spatial_velocity[0]["angular"]["x"], rr_spatial_velocity[0]["angular"]["y"],\
            rr_spatial_velocity[0]["angular"]["z"], rr_spatial_velocity[0]["linear"]["x"], \
            rr_spatial_velocity[0]["linear"]["y"], rr_spatial_velocity[0]["linear"]["z"]])

    def array_to_spatial_acceleration(self, spatial_acceleration, dtype=np.float64):
        ret = self._create_return_np(self._spatial_acceleration_type, dtype)
        ret[0]["angular"]["x"] = spatial_acceleration[0]
        ret[0]["angular"]["y"] = spatial_acceleration[1]
        ret[0]["angular"]["z"] = spatial_acceleration[2]
        ret[0]["linear"]["x"] = spatial_acceleration[3]
        ret[0]["linear"]["y"] = spatial_acceleration[4]
        ret[0]["linear"]["z"] = spatial_acceleration[5]
        return ret

    def spatial_acceleration_to_array(self, rr_spatial_acceleration):
        return np.array([rr_spatial_acceleration[0]["angular"]["x"], rr_spatial_acceleration[0]["angular"]["y"],\
            rr_spatial_acceleration[0]["angular"]["z"], rr_spatial_acceleration[0]["linear"]["x"], \
            rr_spatial_acceleration[0]["linear"]["y"], rr_spatial_acceleration[0]["linear"]["z"]])

    
    def array_to_wrench(self, wrench, dtype=np.float64):
        ret = self._create_return_np(self._wrench_type, dtype)
        ret[0]["torque"]["x"] = wrench[0]
        ret[0]["torque"]["y"] = wrench[1]
        ret[0]["torque"]["z"] = wrench[2]
        ret[0]["force"]["x"] = wrench[3]
        ret[0]["force"]["y"] = wrench[4]
        ret[0]["force"]["z"] = wrench[5]
        return ret

    def wrench_to_array(self, rr_wrench):
        return np.array([rr_wrench[0]["torque"]["x"], rr_wrench[0]["torque"]["y"],\
            rr_wrench[0]["torque"]["z"], rr_wrench[0]["force"]["x"], \
            rr_wrench[0]["force"]["y"], rr_wrench[0]["force"]["z"]])

    
