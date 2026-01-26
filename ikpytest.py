from ikpy.chain import Chain

robot_chain = Chain.from_urdf_file(
    "franka_emika_panda/panda.urdf",
    base_elements=["panda_link0"]
)

print(robot_chain)
