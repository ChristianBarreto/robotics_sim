import mujoco
from mujoco import viewer
from controls import PositionController

MODEL_PATH = "../mujoco_menagerie/franka_emika_panda/scene.xml"

def main():
    model = mujoco.MjModel.from_xml_path(MODEL_PATH)
    data = mujoco.MjData(model)

    controller = PositionController(model)

    # alvo articular visível
    controller.q_des = [
 0.6075,
 -1.6649,
 -0.2630,
 -0.5003,
 -0.7765,
 0.1856,
 0.0000,
0.0000
]
    with viewer.launch_passive(model, data) as v:
        while v.is_running():
            data.ctrl[:] = controller.compute(data)
            mujoco.mj_step(model, data)
            v.sync()   # 🔴 ESSENCIAL

if __name__ == "__main__":
    main()
