import { Box, Chip } from "@mui/material";
import { useCurrentRefinements } from "react-instantsearch";
import HighlightOffIcon from "@mui/icons-material/HighlightOff";

const SearchCurrentRefinements = function (): JSX.Element {
  const { items, refine } = useCurrentRefinements();

  return (
    <Box className="flex flex-row flex-wrap gap-2 justify-center">
      {items.map((item) => (
        <Box className="flex flex-row flex-wrap gap-2">
          {item.refinements.map((refinement) => (
            <Chip
              label={`${refinement.attribute.toUpperCase()}: ${
                refinement.label
              }`}
              size="medium"
              className="text-md p-2 md:p-5 font-thin"
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
