import { Box, Typography } from "@mui/material";

const EmptyFilters = function (): JSX.Element {
  return (
    <Box className="flex flex-col w-full h-full align-middle items-center justify-center gap-2 bg-red">
      <Typography
        className="text-gray-500 align-middle font-mono font-thin"
        variant="body2"
        fontSize="small"
      >
        No results matching the current filters.
      </Typography>
      <Typography
        className="text-gray-500 align-middle font-mono font-thin"
        variant="body2"
        fontSize="small"
      >
        Clear the filters to see all results.
      </Typography>
    </Box>
  );
};

export default EmptyFilters;
