# Stores active session memory
session_memory_store = {}


def save_session_memory(
    session_id,
    data
):

    session_memory_store[session_id] = data


def get_session_memory(
    session_id
):

    return session_memory_store.get(
        session_id,
        {}
    )


def clear_session_memory(
    session_id
):

    if session_id in session_memory_store:

        del session_memory_store[session_id]