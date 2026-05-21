# Long-term patient memory

patient_memory_store = {}


def save_patient_memory(
    patient_name,
    memory_data
):

    patient_memory_store[
        patient_name
    ] = memory_data


def get_patient_memory(
    patient_name
):

    return patient_memory_store.get(
        patient_name,
        {}
    )