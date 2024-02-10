import { Box, Chip } from "@mui/material";
import { useCurrentRefinements } from "react-instantsearch";
import HighlightOffIcon from "@mui/icons-material/HighlightOff";

const SearchCurrentRefinements = function (): JSX.Element {
  const { items, refine } = useCurrentRefinements();

  return (
    <Box className="flex flex-row flex-wrap gap-2 p-5 justify-center">
      {items.map((item) => (
        <Box className="flex flex-row flex-wrap">
          {item.refinements.map((refinement) => (
            <Chip
              label={refinement.label}
              size="small"
              className="p-2 md:p-4 font-thin font-mono bg-amber-500 hover:bg-amber-600 hover:text-white"
              deleteIcon={<HighlightOffIcon />}
              onDelete={() => refine(refinement)}
            />
          ))}
        </Box>
      ))}
    </Box>
  );
};

export default SearchCurrentRefinements;
