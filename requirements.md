# Requirements

 * Excercises are automatically sent to out inbox (organized and formatted).
 * Workouts are sent with examples in case we don't remember or know the excercise by name.
 * Workouts follow a predefined program.
 * Can easily implement / add new exercises / programs.

# Design

  * Workout program
    * Workout (Days)
        * Routines
            * Excercises
  
  * Excercise
    - Name
    - Url (to show example of excercise)
  * Routine
    - Name
    - Instructions
    - Excercises (iterable of exercise objects)
  * Workout
    - Name
    - Routines
  * Workout Program
    - Schedule of days <> Workouts
    - 