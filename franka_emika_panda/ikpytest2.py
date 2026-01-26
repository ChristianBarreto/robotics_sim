import numpy as np
from ikpy.chain import Chain
from ikpy.link import OriginLink, URDFLink


# ==========================================================
# Carrega a cadeia cinemática a partir do URDF
# ==========================================================
# Ajuste o caminho para onde você salvar o URDF
URDF_PATH = "franka_emika_panda/panda_ik.urdf"

panda_chain = Chain.from_urdf_file(
    URDF_PATH,
    base_elements=["base"],
)


# ==========================================================
# Função de IK
# ==========================================================

def compute_ik(target_xyz, direction=None):
    angles = panda_chain.inverse_kinematics(target_xyz, direction)
    return angles[1:]  # remove OriginLink



# ==========================================================
# Exemplo de uso
# ==========================================================
if __name__ == "__main__":
    target_xyz = [-0.5, -0.5, 0.5]  # metros

    # target_xyz = [1, 1, 1]  # metros

    angles = compute_ik(target_xyz)

    print("Ângulos das juntas (rad):")
    print("[")
    for i, angle in enumerate(angles, start=1):
        print(f" {angle:.4f},")
    print("0.0000")
    print("]")

    print(angles)
