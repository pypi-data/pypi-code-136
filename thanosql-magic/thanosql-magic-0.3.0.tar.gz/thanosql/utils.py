import pandas as pd
from IPython.display import Audio, Image, Video, display
from psycopg2 import connect
from sqlalchemy import create_engine

from thanosql.exceptions import ThanoSQLInternalError, ThanoSQLConnectionError


def format_result(output_dict: dict):

    data = output_dict["data"]
    workspace_db_info = data.get("workspace_db_info")
    query_string = data.get("query_string")
    response_type = data.get("response_type")
    extra_query_string = data.get("extra_query_string")
    
    user = workspace_db_info.get("user")
    password = workspace_db_info.get("password")
    database = workspace_db_info.get("database")
    host = workspace_db_info.get("host")

    connection_string = f"postgresql://{user}:{password}@/{database}?host={host}"

    try:
        engine = create_engine(connection_string)
    except:
        raise ThanoSQLConnectionError("Error connecting to workspace database")

    with engine.connect() as conn:
        
        if response_type == "NORMAL":
            try:
                result = pd.read_sql_query(query_string, conn)
            except:
                print("Success")
                return

        elif response_type == "SELECT":
            result = pd.read_sql_query(query_string, conn)

        elif response_type == "SELECT_DROP":
            result = pd.read_sql_query(query_string, conn)
            conn.execute(extra_query_string)

        elif response_type is None:
            print("Success")
            return
            
        else:
            raise ThanoSQLInternalError("Invalid Response Type")
            
    
    print_type = data.get("print")
    if print_type:
        print_option = data.get("print_option", {})
        return print_result(result, print_type, print_option)

    return result


def print_result(query_df, print_type: str, print_option):
    if print_type == "print_image":
        return print_image(query_df, print_option)
    elif print_type == "print_audio":
        return print_audio(query_df, print_option)
    elif print_type == "print_video":
        return print_video(query_df, print_option)
    else:
        raise ThanoSQLInternalError("Error: Wrong print_type.")


def print_image(df, print_option):
    column_name = print_option.get("image_column", "image_path")
    image_file_list = list(df[column_name])

    base_dir = print_option.get("base_dir", "")
    limit = print_option.get("limit")
    for image_path in image_file_list[:limit]:
        image_full_path = f"{base_dir}/{image_path}"
        print(image_full_path)
        display(Image(image_full_path, width=240, height=240))
    return


def print_audio(df, print_option):
    column_name = print_option.get("audio_column", "audio_path")
    audio_file_list = list(df[column_name])

    base_dir = print_option.get("base_dir", "")
    limit = print_option.get("limit")
    for audio_path in audio_file_list[:limit]:
        audio_full_path = f"{base_dir}/{audio_path}"
        print(audio_full_path)
        display(Audio(audio_full_path))
    return


def print_video(df, print_option):
    column_name = print_option.get("video_column", "video_path")
    video_file_list = list(df[column_name])

    base_dir = print_option.get("base_dir", "")
    limit = print_option.get("limit")
    for video_path in video_file_list[:limit]:
        video_full_path = f"{base_dir}/{video_path}"
        print(video_full_path)
        display(Video(video_full_path, embed=True))
    return