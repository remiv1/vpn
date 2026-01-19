from typing import Any

def create_packet(payload: Any) -> dict[str, Any]:
    return {
        "payload": payload
    }

def encapsulate(packet: dict[str, Any], tunnel_type: str = "TUNNEL-1") -> dict[str, object]:
    return {
        "tunnel_header": {
            "type": tunnel_type,
            "length": len(str(packet))
        },
        "inner_packet": packet
    }

def decapsulate(encapsulated_packet: dict[str, object]) -> Any:
    return encapsulated_packet["inner_packet"]

if __name__ == "__main__":
    # Création du paquet original
    packet = create_packet({"message": "Bonjour Rémi", "id": 42})

    print("Paquet original :", packet)

    # Encapsulation
    encap = encapsulate(packet, tunnel_type="GRE")
    print("\nEncapsulé :", encap)

    # Décapsulation
    decap = decapsulate(encap)
    print("\nDécapsulé :", decap)
