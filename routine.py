import random
import exercise
import itertools

class ExerciseRoutine(object):
    """Interface to define an exercise routine.

    Routines are instructionss / notes combined with a set of exercises. Typically,
    they will represent one group, or part, of a full workout.
    """    
    def __init__(self, name, instructions, exercises):
        """Constructor for the ExerciseRoutine object.

        Args:
            name: `string` The name of hte routine.
            instructions: `string` Instructions for the routine.
            exercises: `list` A list of `Exercise` objects that make up the routine.
        """
        self.name = name
        self.instructions = instructions
        self.exercises = exercises
        
        self.exercises_for_routine = []
        
    def get_exercises(self):
        """Randomly chooses and returns exercises for the routine.

        Exercises will not repeat.

        Returns:
            A `list` of `Exercise` objects.
        """
        if not self.exercises_for_routine:
            self.exercises_for_routine.append(random.choice(self.exercises))
        
        return self.exercises_for_routine
    
    def as_html(self):
        """Formats the routine as a list element with a nested list of exercises.

        Returns:
            A `string` formatted as an html list.
        """
        exercises_formatted = ''.join(
            [f"<li>{exercise}</li>" for exercise in self.get_exercises()]
        )
        return f"""
            <li><b>{self.name}</b> {self.instructions.rstrip(".")}:
                <ul>
                    {exercises_formatted}
                </ul>
            </li>"""
    
    def __str__(self):
        return self.as_html()
    

class SupersetRoutine(ExerciseRoutine):
    """Interface for a superset routine.

    This is a slight derivation from a normal exercise routine.
    """    
    def __init__(self, name, instructions, exercise_groups):
        _unused_exercises = itertools.chain.from_iterable(exercise_groups)
        super().__init__(name, instructions, _unused_exercises)
        self.exercise_groups = exercise_groups
        
    def get_exercises(self):
        """Overwrites the get_exercises method to work with an exercise list of lists."""
        if not self.exercises_for_routine:
            for exercise_group in self.exercise_groups:
                self.exercises_for_routine.append(random.choice(exercise_group))
        
        return self.exercises_for_routine
    

PressRoutine = SupersetRoutine(
    name="Press routine",
    instructions="Superset! Perform 3-4 supersets of 8-12 reps of each exercise.",
    exercise_groups=[
        [
            exercise.DBFloorPress,
            exercise.BarbellFloorPress,
        ], [
            exercise.FlatDBBenchPress,
            exercise.InclineDBBenchPress,
        ]
    ]
)

Traps = ExerciseRoutine(
    name="Traps",
    instructions="Perform 3-4 sets of 10 reps.",\
    exercises=[
        exercise.DBShrugs,
        exercise.BarbellShrugs,
    ]    
)