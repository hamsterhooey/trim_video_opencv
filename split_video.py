import cv2
import argparse


def extract_clip(video_path, time_begin, time_end):

    cap = cv2.VideoCapture(video_path)
    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_count = cap.get(cv2.CAP_PROP_FRAME_COUNT)
    duration = int(frame_count / fps)
    if time_begin < 0 or time_end > duration:
        raise ValueError('Invalid time inputs')
        return -1

    start_frame = time_begin * fps
    end_frame = time_end * fps
    cap.set(cv2.CAP_PROP_POS_FRAMES, start_frame)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    # video.get(3) is the horizontal dimension of the video
    out = cv2.VideoWriter('output_{}_{}.avi'.format(time_begin, time_end), fourcc, fps, (int(cap.get(3)), int(cap.get(4))))

    current_frame = start_frame
    while(cap.isOpened()):
        current_frame += 1
        ret, frame = cap.read()
        out.write(frame)
        if current_frame >= end_frame:
            break

    cap.release()
    cv2.destroyAllWindows()
    print("Successful")


def parse_args():
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("--video_path", help="")
    parser.add_argument("--time_begin", help="")
    parser.add_argument("--time_end", help="")
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    args = parse_args()
    video_path = args.video_path
    time_begin = int(args.time_begin)
    time_end = int(args.time_end)
    extract_clip(video_path, time_begin, time_end)
    """
    Example usage:
    python split_video.py --video_path "/home/srinath/Desktop/Link to object_detection/exported_inference_graph_tap_fracture_root_nodefect/GP003043-041789_20150701_13 18_Downstream_V_Post.mpg" --time_begin 60 --time_end 520
    """
