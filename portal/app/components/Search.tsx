import { Grid, Stack } from "@mui/material";
import { InfiniteHits, useInstantSearch } from "react-instantsearch";
import SearchHit from "./SearchHit";
import SearchBar from "./SearchBar";
import EmptyHits from "./EmptyHits";

const Search = function (): JSX.Element {
  const { results } = useInstantSearch();

  return (
    <Stack className="h-full w-full">
      <SearchBar />
      <Grid container className="flex w-full p-10 overflow-y-auto">
        <Grid item sm={0} md={0} lg={2} />
        <Grid
          item
          sm={12}
          md={12}
          lg={8}
          className="flex flex-col w-full h-full align-middle items-center gap-5"
        >
          {!results.__isArtificial && results.nbHits === 0 ? (
            <EmptyHits />
          ) : (
            <InfiniteHits
              classNames={{
                root: "SearchInfiniteHits",
                list: "SearchInfiniteHitsList",
                item: "SearchInfiniteHitsItem",
              }}
              hitComponent={SearchHit}
              showPrevious={false}
            />
          )}
        </Grid>
        <Grid item sm={0} md={0} lg={2} />
      </Grid>
    </Stack>
  );
};

export default Search;
