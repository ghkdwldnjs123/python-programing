class Movie:
    def __init__(self, title, schedule):
        self.title = title
        self.schedule = schedule 
        self.seats = {time: [False] * 10 for time in schedule}

    def reserve_seat(self, time, seat_number):
        if time not in self.seats:
            print(f"{time}에 상영하는 시간이 없습니다.")
            return
        if not (0 <= seat_number < 10):
            print("좌석 번호는 0에서 9 사이여야 합니다.")
            return

        if self.seats[time][seat_number]:
            print("이미 예약된 좌석입니다.")
        else:
            self.seats[time][seat_number] = True
            print(f"{time}에 {seat_number}번 좌석 예약 완료.")

    def get_available_seats(self, time):
        if time not in self.seats:
            print(f"{time}에 상영하는 시간이 없습니다.")
            return 0
        return self.seats[time].count(False)


class Theater:
    def __init__(self):
        self.movies = {}

    def add_movie(self, title, schedule):
        if title in self.movies:
            print(f"이미 등록된 영화입니다: {title}")
            return
        movie = Movie(title, schedule)
        self.movies[title] = movie
        print(f"영화 추가: {title}, 상영 시간표: {schedule}")

    def reserve_movie_seat(self, title, time, seat_number):
        if title not in self.movies:
            print(f"존재하지 않는 영화입니다: {title}")
            return
        movie = self.movies[title]
        movie.reserve_seat(time, seat_number)

    def get_movie_schedule(self, title):
        if title not in self.movies:
            print(f"존재하지 않는 영화입니다: {title}")
            return
        movie = self.movies[title]
        print(f"영화 제목: {title}")
        for time in movie.schedule:
            available_seats = movie.get_available_seats(time)
            print(f"{time} - 예약 가능한 좌석: {available_seats}")

theater = Theater()
theater.add_movie("청설", ["10:00", "12:30", "14:15"])
theater.add_movie("판도라", ["12:15", "14:00", "16:45"])

theater.reserve_movie_seat("청설", "10:00", 3)
theater.reserve_movie_seat("청설", "10:00", 3)
theater.reserve_movie_seat("판도", "12:00", 5)

theater.get_movie_schedule("청설")
theater.get_movie_schedule("판도")
