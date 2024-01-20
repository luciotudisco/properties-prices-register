import { Grid, Stack, Typography } from "@mui/material";
import { InfiniteHits, useInstantSearch, useStats } from "react-instantsearch";
import SearchHit from "./SearchHit";
import SearchBar from "./SearchBar";
import EmptyHits from "./EmptyHits";

const Search = function (): JSX.Element {
  const { results } = useInstantSearch();
  const { nbHits } = useStats();

  return (
    <Stack className="h-full w-full">
      <SearchBar />
      <Grid container className="flex w-full h-full p-5 overflow-y-auto">
        <Grid item sm={0} md={0} lg={2} />
        <Grid
          item
          sm={12}
          md={12}
          lg={8}
          className="flex flex-col w-full h-full align-middle items-center gap-2"
        >
          {!results.__isArtificial && results.nbHits === 0 ? (
            <EmptyHits />
          ) : (
            <>
              <Typography
                className="text-gray-400"
                variant="caption"
                fontSize="small"
              >
                {nbHits} results found
              </Typography>
              <InfiniteHits
                classNames={{
                  root: "SearchInfiniteHits",
                  list: "SearchInfiniteHitsList",
                  item: "SearchInfiniteHitsItem",
                }}
                hitComponent={SearchHit}
                showPrevious={false}
              />
            </>
          )}
        </Grid>
        <Grid item sm={0} md={0} lg={2} />
      </Grid>
    </Stack>
  );
};

export default Search;
