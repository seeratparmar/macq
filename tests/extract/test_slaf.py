from macq.extract import Extract, modes
from macq.observation import PartialObservation
from tests.utils.generators import generate_blocks_traces


if __name__ == "__main__":
    traces = generate_blocks_traces(plan_len=2, num_traces=1)
    observations = traces.tokenize(
        PartialObservation,
        method=PartialObservation.random_subset,
        percent_missing=0.10,
    )
    model = Extract(observations, modes.SLAF)
    print()
    print(model.details())